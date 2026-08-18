---
title: "Local-First Secrets for AI Agents on macOS: A 2026 Field Survey"
excerpt: "A field survey of local secret stores for AI agents on macOS—and the privilege boundary needed to keep an agent from erasing its own access trail."
date: 2026-08-06
lang: en
published: true
cover_image:
  src: /assets/blogposts/2026-08-06-local-first-secrets-for-ai-agents-macos-survey/local-first-secrets-ai-agents-macos-00-cover.jpg
  x: 167
  y: 0
  size: 666
og_image: /assets/blogposts/2026-08-06-local-first-secrets-for-ai-agents-macos-survey/local-first-secrets-ai-agents-macos-00-cover.jpg
categories:
  - blog
tags:
  - security
  - secrets-management
  - ai-agents
  - claude-code
  - macos
---

*What exists today for storing and brokering credentials—strings and files—entirely on one Mac, consumable by coding agents unattended, with an access trail that the agent's own user account cannot directly rewrite. Claims from my hands-on testing are labeled as such.*

This survey is the technical companion to [I Didn't Know Where My Keys Had Leaked, So I Started Building GuestSafe](/blog/why-i-started-building-guestsafe/). The other article tells the personal story and describes the narrow tool I decided to build; this one preserves the broader product research and security reasoning behind that decision.

## TL;DR

I wanted my Claude Code agents to use credentials (Gmail service accounts, API keys, SSH keys) that never leave my machine, work without human prompts, and leave a local access trail. I surveyed six categories of tooling—server-style secrets managers, password-manager vaults, developer secret injectors, agent-era credential brokers, MCP secrets servers, and macOS primitives—against four criteria plus one extra lens I care about: **the home-vault standard**. It is acceptable that malicious code running as my login account can use a credential already delegated to that account, but it should not be able to rewrite the record of that use.

That last sentence needs a precise threat model. Here, "same-user attacker" means an unprivileged process running as my login account. It does **not** include root, Recovery Mode, physical destruction, or an administrator who can reconfigure the logging system. Under that model, the useful boundary is privilege separation: the agent can request a secret, while a different service identity owns the audit trail.

Three conclusions:

1. **Most local vaults and injectors do not record secret reads.** Some commercial products reserve audit features for paid tiers; some "activity logs" record changes rather than reads.
2. **OpenBao is the closest documented fit.** Its audit devices record requests and responses (with documented exceptions), but a file owned by the agent's own account is not a security boundary. Run the daemon or its audit sink under a different service identity if the log must survive compromise of the agent account.
3. **No single macOS primitive is a permanent, unerasable ledger.** Unified-log entries rotate, `sappnd` is reversible by root, and EndpointSecurity products still need protected log storage. The practical local design is privilege separation plus bounded retention; a durable external anchor is stronger but no longer "one Mac only."

## 中文摘要

我调研了 macOS 上为 AI agent 提供“纯本地、支持文件凭证、无人值守、记录读取行为”的六类工具。关键结论不是某个文件标志能让日志永久不可删，而是**权限分离**：agent 可以读取已授权的凭证，但审计日志应由另一个服务身份拥有。OpenBao 是目前最接近这套需求的通用工具；统一日志、`sappnd` 和 EndpointSecurity 可以加固方案，但都不是永久、绝对不可擦除的账本。若把哈希锚点复制到机器之外，证据会更强，但也不再满足“只在一台 Mac 上”的严格定义。

## The requirements

![Four requirements surround a local Mac: local custody, file credentials, unattended access, and an access audit](/assets/blogposts/2026-08-06-local-first-secrets-for-ai-agents-macos-survey/local-first-secrets-ai-agents-macos-01-requirements.jpg)

My constraints, in order of non-negotiability:

- **C1 — Local custody.** No vendor cloud. A localhost-only daemon is fine; SaaS is not.
- **C2 — File credentials.** A secret is an arbitrary byte blob — a GCP service-account JSON, an OAuth client secret file, a PEM key — not just an env-var string. Plain `.env` doesn't cover this.
- **C3 — Unattended.** Agents fetch secrets with zero human prompts. macOS Keychain can do this for items whose access control already trusts the calling application, but that choice trades prompts for a broader standing authorization.
- **C4 — Access audit.** A local record of who/what read which secret, when.

Plus the lens that reframes C4: **tamper resistance against the agent account**. A log file owned by my login account can be erased by malicious code running as that account—they hold the same pen. The practical question is therefore: can the agent cause an auditable operation while a different identity owns the resulting record?

## Master table

Here, C4 means that the product documents a record of secret reads or API requests. It does **not** mean the record is tamper-resistant; that depends on who owns the logger and its storage. A dash means the tool is out of scope for the criterion, while “not verified” means I did not find sufficiently specific public documentation.

| Tool | C1 Local | C2 Files | C3 Unattended | C4 Audit | Status 2026 |
|---|---|---|---|---|---|
| [OpenBao](https://openbao.org/) | ✅ | ⚠️ base64 KV | ✅ | ✅ API request/response audit, free | active (Linux Foundation) |
| [Vault](https://www.hashicorp.com/en/blog/hashicorp-adopts-business-source-license) | ✅ | ⚠️ base64 KV | ✅ | ✅ per-request | BUSL license |
| [Infisical self-hosted](https://infisical.com/docs/self-hosting/deployment-options/docker-compose) | ⚠️ local, heavy | ⚠️ values/base64 | ✅ | ❌ enterprise paywall | active |
| [Conjur OSS](https://github.com/cyberark/conjur/releases) | ✅ | ⚠️ values | ✅ | ❌ officially Enterprise-only | maintained, heavyweight |
| [Keywhiz](https://github.com/square/keywhiz) | — | — | — | — | dead (archived 2023) |
| [KeePassXC](https://keepassxc.org/) | ✅ | ✅ attachments | ⚠️ password/key file | ❌ no per-read log documented | active |
| [Vaultwarden](https://github.com/dani-garcia/vaultwarden) + bw | ✅ | ✅ attachments | ✅ | ⚠️ org events only | active |
| [1Password](https://support.1password.com/migrate-1password-account/) | ❌ cloud only | ✅ documents | ✅ | ⚠️ cloud-side | no local mode |
| [Psono](https://doc.psono.com/admin/configuration/audit-log.html) | ✅ | ⚠️ not verified | ✅ | ⚠️ EE tier | active |
| [Passbolt CE](https://www.passbolt.com/pricing) | ✅ | ❌ | ✅ | ❌ no per-read log documented | active |
| [pass / gopass](https://github.com/gopasspw/gopass) | ✅ | ✅ gopass | ✅ | ❌ no read log documented | active |
| macOS Keychain (CLI) | ✅ | ⚠️ generic-password data; CLI caveats | ✅ with pre-authorized ACL | ❌ no supported per-item read log found | usable with tradeoffs |
| [sops](https://github.com/getsops/sops) + [age](https://formulae.brew.sh/formula/age) | ✅ | ✅ structured/binary modes | ✅ | ❌ no read log documented | active |
| [SecretSpec](https://github.com/cachix/secretspec) | ✅ provider choice | ⚠️ not verified | ✅ | ✅ local access log | young (2025) |
| [novops](https://github.com/PierreBeucher/novops) | ✅ via sops | ✅ in-mem files | ✅ | ❌ no read log documented | active |
| [dotenvx](https://github.com/dotenvx/dotenvx) | ✅ | ⚠️ env values | ✅ | ❌ no read log documented | active |
| [fnox](https://github.com/jdx/fnox) | ✅ | ⚠️ not verified | ✅ | ⚠️ not verified | new, active |
| [vals](https://github.com/helmfile/vals) | ✅ sops/keychain | ❌ values only | ✅ | ❌ no read log documented | active |
| [envchain](https://github.com/sorah/envchain) | ✅ keychain | ❌ | ✅ | ❌ no read log documented | frozen 2024 |
| [aws-vault](https://github.com/99designs/aws-vault) | ✅ | ❌ AWS only | ✅ | ❌ no read log documented | abandoned; [fork](https://github.com/ByteNess/aws-vault) alive |
| [teller](https://github.com/tellerops/teller/releases) | ⚠️ dotenv only | ❌ | ✅ | ❌ no read log documented | semi-dormant |
| [chamber](https://github.com/segmentio/chamber) | ❌ AWS | ❌ | ✅ | ⚠️ CloudTrail | active |
| [Pomerium](https://www.pomerium.com/docs/capabilities/mcp) | ✅ self-hostable | ❌ tokens | ✅ | ✅ request log | active |

## A. Server-style secrets managers

![An agent sends secret requests to a local service while a separate identity owns the audit ledger](/assets/blogposts/2026-08-06-local-first-secrets-for-ai-agents-macos-survey/local-first-secrets-ai-agents-macos-02-server-managers.jpg)

**OpenBao** is [a fork of Vault managed under the Linux Foundation](https://openbao.org/#:~:text=fork%20of%20Vault%20managed%20by%20the%20Linux%20Foundation) and is MPL-2.0 licensed. It has the best-documented free audit path in this survey: an audit device records requests and responses for nearly every API operation, including errors, with a [short list of unaudited system paths](https://openbao.org/docs/audit/#:~:text=The%20non%2Daudited%20paths%20are). Most sensitive strings are [salted HMAC-SHA256 values rather than plaintext](https://openbao.org/docs/audit/#:~:text=Most%20strings%20contained%20within%20requests%20and%20responses%20are%20hashed). Auditing is off on a newly initialized server and must be [enabled by an OpenBao root-policy user](https://openbao.org/docs/audit/#:~:text=When%20an%20OpenBao%20server%20is%20first%20initialized%2C%20no%20auditing%20is%20enabled). OpenBao supports file, socket, syslog, and HTTP audit devices and recommends enabling more than one. It also offers a [filesystem storage backend](https://openbao.org/docs/configuration/storage/filesystem/#:~:text=The%20Filesystem%20storage%20backend%20stores%20OpenBao%27s%20data), although the project warns that this backend is not recommended for production because it is non-transactional and lacks system-level file locking.

Two operational gotchas matter on a Mac. Since OpenBao 2.4, [declarative self-initialization and audit-device configuration](https://openbao.org/blog/features-declarative-configuration/) remove some manual setup, but [fully unattended self-initialization still requires Auto Unseal](https://openbao.org/docs/configuration/self-init/). The [Homebrew formula](https://formulae.brew.sh/formula/openbao) installs the `bao` binary, while the tempting `bao server -dev` path [stores data in memory and loses it on restart](https://openbao.org/docs/concepts/dev-server/#:~:text=lose%20data%20on%20every%20restart). A durable deployment still needs a real seal, storage, identity, listener, policy, audit, backup, and upgrade plan. More importantly, a file audit device inherits the protection of its host account. If OpenBao and the agent both run as my login user, malicious code can remove the file. If OpenBao or a local audit collector runs as a dedicated service identity and its directory is not writable by my login user, the same agent token can fetch secrets without gaining the ability to rewrite the log. That privilege boundary, not the file format, provides the useful protection.

**Vault** itself has the same audit capability but has been [Business Source License 1.1 since August 2023](https://www.hashicorp.com/en/blog/hashicorp-adopts-business-source-license#:~:text=to%20the%20Business%20Source%20License) ([v1.15.0 and later](https://github.com/hashicorp/vault/blob/main/LICENSE), each release converting to MPL 2.0 four years out), and HashiCorp is now IBM, which [completed the $6.4 billion acquisition in February 2025](https://newsroom.ibm.com/2025-02-27-ibm-completes-acquisition-of-hashicorp,-creates-comprehensive,-end-to-end-hybrid-cloud-platform#:~:text=enterprise%20value%20of%20%246.4%20billion). OpenBao is the open path to the same architecture.

**Infisical self-hosted** (my incumbent, via its cloud) runs as [the app plus PostgreSQL plus Redis](https://infisical.com/docs/self-hosting/deployment-options/docker-compose#:~:text=Redis%20for%20caching%20and%20job%20queues), minimum 2 CPU / 4 GB RAM. The core repo is [MIT except the `ee` directory of enterprise features](https://github.com/Infisical/infisical#:~:text=premium%20enterprise%20features%20requiring). The dealbreaker: audit logs are a paid feature — self-hosters are told to [contact sales to purchase an enterprise license](https://infisical.com/docs/documentation/platform/audit-logs#:~:text=purchase%20an%20enterprise%20license) to use them.

**Conjur OSS** is still maintained ([v1.24.0 in November 2025](https://github.com/cyberark/conjur/releases/tag/v1.24.0)) and offers policy-as-code, but CyberArk staff state that [audit logging is officially supported only in Conjur Enterprise](https://discuss.cyberarkcommons.org/t/can-i-get-audit-logs-via-rest-api/1331/2). That removes it from C4 and leaves a PostgreSQL-backed, enterprise-shaped system for a single Mac. **Keywhiz** is [deprecated and no longer maintained](https://github.com/square/keywhiz#:~:text=this%20project%20is%20now%20deprecated%20and%20no%20longer%20maintained); Square points users to Vault.

## B. Password-manager vaults with CLIs

![A local password vault can hold strings and files, but opening it does not necessarily create a read ledger](/assets/blogposts/2026-08-06-local-first-secrets-for-ai-agents-macos-survey/local-first-secrets-ai-agents-macos-03-password-vaults.jpg)

**KeePassXC** is the simplest fully local vault in the set: a single KDBX file, with real file-credential support via `keepassxc-cli`—[`attachment-export` writes an attachment to a specified file](https://man.archlinux.org/man/keepassxc-cli.1.en#:~:text=Exports%20the%20content%20of%20an%20attachment%20to%20a%20specified%20file). Unattended use can supply a password on standard input or use a key file with the CLI's `--key-file` and `--no-password` options; either way, the automation still needs custody of unlocking material. Its Secret Service integration [acts as a Secret Service provider over D-Bus](https://keepassxc.org/docs/KeePassXC_UserGuide.html#:~:text=act%20as%20a%20Secret%20Service%20provider%20over%20DBus), a freedesktop.org facility rather than a macOS Keychain interface. I found no documented per-entry read log.

**Vaultwarden** — the [unofficial Bitwarden-compatible server written in Rust](https://github.com/dani-garcia/vaultwarden#:~:text=Unofficial%20Bitwarden%20compatible%20server%20written%20in%20Rust), AGPL-3.0 — gives genuinely local custody with the official `bw` CLI, which supports unattended auth via API key and [`--passwordenv` / `--passwordfile` unlock](https://bitwarden.com/help/cli/#:~:text=retrieve%20your%20master%20password%20rather%20than%20enter%20it%20manually). Audit is the weak leg: Bitwarden event logs are [records that capture changes and usage across your Teams or Enterprise organization](https://bitwarden.com/help/event-logs/#:~:text=capture%20changes%20and%20usage%20across%20your%20Teams%20or%20Enterprise%20organization) — organization-scoped, so your own personal-vault reads aren't meaningfully covered. In Vaultwarden, org events are [only stored in the database](https://github.com/dani-garcia/vaultwarden/discussions/3545#:~:text=only%20stored%20in%20the%20database) — the maintainer explicitly declined file/SIEM output. And the `bws` Secrets Manager won't work against Vaultwarden: [that feature is Bitwarden-licensed, not open-source licensed](https://github.com/dani-garcia/vaultwarden/discussions/5702#:~:text=Bitwarden%20licensed%20and%20not%20open%20source%20licensed); self-hosting it officially [requires an enterprise plan](https://bitwarden.com/blog/enterprise-self-hosting-for-bitwarden-secrets-manager/#:~:text=on%20enterprise%20plans%20can%20bring%20the%20same).

**1Password**—evaluated honestly since I already use it for browser autofill—has no current standalone-vault mode. [1Password 8 requires a 1Password membership](https://support.1password.com/migrate-1password-account/#:~:text=1Password%208%20requires%20a%201Password%20membership); the same page says [1Password 7 and earlier supported standalone vaults](https://support.1password.com/migrate-1password-account/#:~:text=1Password%207%20and%20earlier%20supported%20standalone%20vaults). The self-hostable Connect server [caches data in your infrastructure](https://www.1password.dev/connect/#:~:text=cache%20your%20data%20in%20your%20infrastructure) but syncs with 1password.com, so it reduces runtime cloud dependence rather than providing local custody. Credit where due: the Environments MCP server [exposes variable names but not secret values](https://www.1password.dev/environments/mcp-server#:~:text=only%20sees%20variable%20names) and injects values into an authorized process via a local in-memory FIFO. It is not unattended in the sense used here: the current walkthrough says [every interaction requires explicit user approval](https://www.1password.dev/environments/mcp-server#:~:text=Every%20interaction%20requires%20explicit%201Password%20user%20authorization%20prompt%20approval).

**Psono** has an automation CLI ([psonoci, built for CI](https://github.com/meldron/psonoci#:~:text=secure%20access%20to%20your%20psono%20passwords)), but its audit log is [only available in the Enterprise Edition](https://doc.psono.com/admin/configuration/audit-log.html#:~:text=only%20available%20in%20the%20Enterprise%20Edition). General encrypted file attachments remain [listed as a Passbolt feature request](https://community.passbolt.com/c/backlog/6#:~:text=create%20resources%20with%20encrypted%20file%20attachement), and its paid [activity log is described as auditing changes](https://www.passbolt.com/pricing#:~:text=Activity%20log%20%28audit%20changes%29), not as a per-secret read ledger. **pass/gopass** are fully local, and gopass supports [binary files through the `cat`, `fscopy`, `fsmove`, and `sum` subcommands](https://github.com/gopasspw/gopass/blob/master/docs/features.md#:~:text=binary%20files%20through%20the), but Git history records writes, not decryptions. Gopass's `audit` command [checks passwords for common flaws](https://github.com/gopasspw/gopass/blob/master/docs/features.md#:~:text=check%20your%20passwords%20for%20common%20flaws); it is a password-quality audit, not access logging.

## C. Developer secret-injection tools

![A trusted injector supplies credentials directly to an authorized process while the agent handles only names and operations](/assets/blogposts/2026-08-06-local-first-secrets-for-ai-agents-macos-survey/local-first-secrets-ai-agents-macos-04-injectors.jpg)

**SecretSpec** ([announced in July 2025](https://devenv.sh/blog/2025/07/21/announcing-secretspec-declarative-secrets-management) by the devenv/Cachix team) is the standout design. A committed `secretspec.toml` declares *what* secrets an application needs while values live in a pluggable provider, including Keyring, KeePass KDBX, pass/gopass, age, 1Password, OpenBao, and others. It is the only injector in this survey whose public documentation advertises built-in access auditing: [every secret access is recorded locally, auditing is on by default, and values are not logged](https://github.com/cachix/secretspec#:~:text=Every%20secret%20access%20recorded%20locally). It is still young, and I have not verified arbitrary file-credential materialization.

**novops** (LGPL-3.0) has the best file-credential ergonomics: its config materializes secrets as [in-memory files with an environment variable pointing at the path](https://github.com/PierreBeucher/novops#:~:text=will%20point%20to%20secure%20in%2Dmemory%20file)—exactly the `GOOGLE_APPLICATION_CREDENTIALS` pattern—with SOPS among its local-capable sources. Its documentation does not advertise a per-read audit log.

**dotenvx**, [from the creator of dotenv](https://github.com/dotenvx/dotenvx#:~:text=from%20the%20creator%20of), encrypts `.env` files with [ECIES; each secret uses a unique ephemeral key](https://github.com/dotenvx/dotenvx#:~:text=Elliptic%20Curve%20Integrated%20Encryption%20Scheme), while you keep the private key in a gitignored `.env.keys`. Its documentation does not advertise a read audit. **fnox**, from mise author jdx, [manages secrets with encryption or cloud providers](https://github.com/jdx/fnox#:~:text=Manage%20secrets%20with%20encryption%20or%20cloud%20providers), including age, OS Keychain, KeePass, and password-store providers. [Mise's secrets documentation recommends fnox](https://mise.jdx.dev/environments/secrets/#:~:text=Full%2Dfeatured%20secret%20manager%20with%20remote%20secret%20storage) over its experimental SOPS/age integration. **vals** resolves `ref+backend://` references with local backends including SOPS and files, plus [a macOS Keychain backend](https://github.com/helmfile/vals#:~:text=It%20reads%20a%20secret%20from%20the%20macOS%20Keychain).

The older generation: **envchain** [stores env vars in macOS Keychain or D-Bus secret service](https://github.com/sorah/envchain#:~:text=envchain%20supports%20macOS%20keychain%20and%20D%2DBus%20secret%20service) but hasn't had a commit since its April 2024 release. **aws-vault**'s README states [the project has been abandoned](https://github.com/99designs/aws-vault#:~:text=This%20project%20has%20been%20abandoned), with a [maintained fork at ByteNess](https://github.com/ByteNess/aws-vault#:~:text=This%20is%20a%20maintained%20fork) — AWS-only either way. **chamber** [stores secrets in SSM Parameter Store](https://github.com/segmentio/chamber#:~:text=it%20does%20so%20by%20storing%20secrets%20in%20SSM%20Parameter%20Store) — AWS-coupled, no local backend. **teller**'s last release was [v2.0.7](https://github.com/tellerops/teller/releases#:~:text=v2.0.7) in May 2024.

Among the injector documentation I checked, SecretSpec is the only project that explicitly promises a local access record. Absence from documentation is not proof that no debug or system log exists; it means I would not select the tool to satisfy C4 without testing and a documented retention contract.

## D. Agent-era credential brokers and MCP

![An agent invokes a brokered tool while the credential remains outside model context](/assets/blogposts/2026-08-06-local-first-secrets-for-ai-agents-macos-survey/local-first-secrets-ai-agents-macos-05-mcp-brokers.jpg)

The new product category built around agents needing credentials is mostly SaaS; managed-auth products therefore fail C1 by design. The self-hostable exception in this survey is **Pomerium**, an identity-aware proxy that [manages upstream OAuth and injects the token into proxied requests without exposing it to clients](https://www.pomerium.com/docs/capabilities/mcp#:~:text=Injects%20the%20upstream%20token%20into%20proxied%20requests%20transparently). It supports service accounts for autonomous agents and [logs every tool call with the method, tool name, and parameters](https://www.pomerium.com/docs/capabilities/mcp#:~:text=Every%20tool%20call%20is%20logged). Architecturally, that is useful, but it brokers API calls rather than materializing file credentials and adds another resident service.

**An MCP tool that returns raw secret values is usually the wrong boundary.** HashiCorp ships an official Vault MCP server ([public beta since HashiConf 2025](https://www.hashicorp.com/en/blog/strengthen-security-with-vault-boundary-and-radar-features-at-hashiconf-2025#:~:text=MCP%20server%20is%20now%20in%20public%20beta)) whose tools include [reading and writing secrets in KV mounts](https://developer.hashicorp.com/vault/docs/mcp-server/overview#:~:text=secrets%20to%20KV%20mounts). In an ordinary MCP client, the result of a read tool can enter the model-visible transcript; that is an architectural inference, not a claim that every client stores every result. Frank Denis's critique captures the principle: [the model does not need the token](https://00f.net/2025/06/16/leaky-mcp-servers/#:~:text=The%20model%20literally%20does%20not%20need%20your%20token). GitGuardian reported [24,008 unique secrets in MCP-related configuration files on public GitHub, including 2,117 valid credentials](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/#:~:text=24%2C008%20unique%20secrets), while OWASP's MCP Top 10 begins with token mismanagement and notes that developers put credentials in [configuration files, environment variables, prompt templates, and model context](https://owasp.org/www-project-mcp-top-10/2025/MCP01-2025-Token-Mismanagement-and-Secret-Exposure#:~:text=Developers%20frequently%20mishandle%20these%20secrets). The safer pattern is to let the agent name an operation or variable while a trusted process injects the value outside model context.

**Claude Code itself** ships relevant primitives. On macOS, its own authentication credentials are [stored in the encrypted macOS Keychain](https://code.claude.com/docs/en/iam#:~:text=On%20macOS%2C%20credentials%20are%20stored%20in%20the%20encrypted%20macOS%20Keychain), and an [`apiKeyHelper`](https://code.claude.com/docs/en/iam#:~:text=apiKeyHelper) can return an API key at runtime. For sandboxed Bash commands, credential `deny` mode removes named environment variables and blocks configured files. Environment-variable `mask` mode (v2.1.199+) gives the command [a per-session sentinel](https://code.claude.com/docs/en/sandboxing#:~:text=sees%20a%20per%2Dsession%20sentinel%20value) and substitutes the real value only through the sandbox proxy; this requires TLS termination and a trusted user, managed, or command-line settings source. The proxy can [re-sign detected AWS SigV4 requests](https://code.claude.com/docs/en/sandboxing#:~:text=re%2Dsigns%20it%20after%20substituting%20the%20real%20values). File masking (v2.1.221+) is platform-dependent: Linux and WSL2 receive a sentinel copy, while [macOS blocks reads instead of substituting](https://code.claude.com/docs/en/sandboxing#:~:text=macOS%3A%20sandboxed%20commands%20can%27t%20read). An exact `filesystem.denyRead` rule also [holds inside a wider allow](https://code.claude.com/docs/en/sandboxing#:~:text=An%20exact%20deny%20holds%20inside%20a%20wider%20allow). These controls reduce exposure; they do not provide a secret store or a durable read audit by themselves.

## E. OS primitives: where a harder-to-erase trace can come from

![A macOS audit trail combines bounded local logs, append flags, monitoring, and a protected sink](/assets/blogposts/2026-08-06-local-first-secrets-for-ai-agents-macos-survey/local-first-secrets-ai-agents-macos-06-macos-audit.jpg)

The home-vault requirement cannot be met by a log file owned by the compromised account. macOS offers useful building blocks, but none is an infinite, unerasable ledger. Their value is relative to the stated attacker: an unprivileged process running as the agent's login account.

| Primitive | What it gives | Limitation | Cost |
|---|---|---|---|
| `uappnd` flag | append-only file; blocks overwrite/delete | owner, silently (`chflags nouappnd`) | free — guardrail only |
| hash-chained log | internal consistency; edits detectable if head is known | owner, by rewriting the whole chain | free — needs an anchor |
| unified log (`os_log`) | centrally stored records a normal user cannot directly edit | entries rotate; administrators can manage or erase the store | tiny |
| `sappnd` flag | append-only flag set and cleared only by root | root can clear it; not permanent immutability | needs root |
| Santa FAA | logs or **blocks** watched file access by process identity | durability depends on protected telemetry storage and administration | root, FDA, system-extension approval |
| eslogger / FileMonitor | EndpointSecurity stream of file events | a stream is not durable until written to a protected sink | root/FDA requirements vary by tool |
| external copy of a chain head | detects later local rewriting if the external copy is trustworthy | violates the strict "one Mac only" constraint | operational dependency |

The receipts:

- **Keychain is a store, not the read ledger I need.** A 2017 investigation found that useful information about keychain opens [had largely vanished from the unified log](https://eclecticlight.co/2017/11/26/last-week-on-my-mac-vanishing-keychains/#:~:text=useful%20information%20about%20the%20opening%20of%20keychains%20has%20all%20but%20vanished), and I found no current Apple interface promising a per-item read audit. This does not make unattended use impossible: the installed `security` manual says an item can trust a specific application with `-T`, or every application with the explicitly discouraged `-A`, so the correct table entry is “usable with ACL tradeoffs,” not “always prompts.” The classic BSM audit subsystem is [deprecated since macOS 11 and disabled since macOS 14](https://keith.github.io/xcode-man-pages/auditd.8.html#:~:text=deprecated%20since%20macOS%2011.0%2C%20disabled%20since%20macOS%2014.0), with Apple pointing developers to EndpointSecurity. I also reproduced a narrower CLI problem: the interactive `security -i` path is reported to have a [4,096-byte input-line limit](https://github.com/anthropics/claude-code/issues/28901). In my test on macOS 26.4.1, 100 KB and 400 KB blobs round-tripped when passed as hex through an argument, so this is an interactive-input limitation, not evidence of a small Keychain item limit.
- **Unified logging is a useful short-lived anchor, not immutable storage.** On my machine, BSD `logger` messages did not appear in the queries I tried, while a small compiled `os_log` call produced entries retrievable with `log show`. Apple says the unified system centralizes logs in memory and on disk, but also documents that [entries rotate according to space, time, and classification](https://developer.apple.com/documentation/oslog/oslogentrystorecategory#:~:text=Entries%20rotate%20out%20to%20free%20up%20resources). The `log` tool also has an `erase` command. A normal user cannot edit a stored entry in place, which is useful against the agent account, but retention is bounded and an administrator remains stronger than the log.
- **BSD file flags are guardrails with explicit owners.** In my test, `uappnd` allowed append while blocking overwrite and removal, but the owner could clear it. Apple's file-system guide confirms that [`uappnd` is owner-or-root controlled, while `sappnd` is root-only](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemDetails/FileSystemDetails.html#:~:text=SF_APPEND). The earlier claim that `sappnd` requires Recovery Mode to clear was wrong: Apple documents that root can change it.
- **EndpointSecurity monitoring is practical, but the sink still matters.** `eslogger` ships with macOS and [must run as superuser with Full Disk Access](https://keith.github.io/xcode-man-pages/eslogger.1.html#:~:text=must%20be%20run%20as%20super%2Duser), though its manual says it is [not intended as an application API](https://keith.github.io/xcode-man-pages/eslogger.1.html#:~:text=not%20intended%20to%20be%20used%20by%20applications). Objective-See's [FileMonitor outputs JSON](https://objective-see.org/products/utilities.html#:~:text=FileMonitor%20will%20output%20JSON) from the same framework. The purpose-built option is **Santa**: File Access Authorization can [monitor, log, or block access](https://northpole.dev/features/faa/#:~:text=monitor%20and%20log%20access%20or%20even%20block%20access), and its events identify the time, process, path, and decision. Santa can send telemetry to the unified log or to files, so its resistance to deletion depends on the selected sink and who administers the system extension.
- **FileVault is baseline protection for data at rest.** Apple says the disk is decrypted after an authorized user logs in, so FileVault helps against offline theft but not malicious code already executing in that logged-in session. The Secure Enclave is also reachable from the age ecosystem through [age-plugin-se](https://github.com/remko/age-plugin-se), which supports access-control policies from `none` (automatable and hardware-bound) through `current-biometry` and requires [macOS 14 plus a Secure Enclave](https://github.com/remko/age-plugin-se#:~:text=decrypt%20encrypted%20files%2C%20you%20need%20a%20Mac) for key generation and decryption.

## What the survey shows

1. **Read auditing is unusual in lightweight local tools.** SecretSpec documents it; OpenBao documents API-level auditing; several commercial systems reserve it for paid tiers; many "activity logs" track changes rather than reads.
2. **OpenBao is the strongest single product in this survey.** It can meet C1–C4 on one Mac, but the home-vault property comes only when the agent account cannot administer the daemon or its audit sink.
3. **Tamper resistance is a deployment property, not a checkbox.** A dedicated service identity and a root-owned or otherwise protected sink create a meaningful boundary against an unprivileged agent process. Unified logging, Santa, and hash chaining can strengthen that design, but none promises permanent local retention.
4. **The safer agent pattern is capability use without value disclosure.** Secret names and intended operations may enter model context; raw values should be injected into a narrowly authorized process or proxied request. 1Password Environments, Pomerium's upstream-token injection, and Claude Code's mask mode are variations on that idea.
5. **Watch list:** SecretSpec for declarative access records and fnox for local encryption in the mise ecosystem. SecretSpec's log still needs the same privilege-separation treatment if it must survive compromise of the agent account.

## What this led me to build

The survey convinced me that OpenBao is the strongest general-purpose answer, but it also clarified the mismatch. Its complexity buys high availability, dynamic secrets, leases, PKI, and infrastructure-scale lifecycle management. My local agents need a much narrower path: discover a small catalog, request a named credential with context, inject it into one process, and record every result.

That is the space I want [GuestSafe](/blog/why-i-started-building-guestsafe/) to occupy. It is not a smaller OpenBao. It is a good-enough, lightweight, auditable replacement for `.env.local`, with a deliberately limited threat model and a much smaller operating surface.

## Methodology

The survey combines public product documentation with hands-on tests on my Apple-silicon Mac running macOS 26.4.1: Keychain CLI input paths, `chflags` semantics, BSD `logger` versus `os_log`, and the current BSM manual. Inline links point to the specific capability being discussed; text-fragment links (`#:~:text=`) highlight the supporting passage where practical. Product documentation is sufficient evidence for a documented interface or edition boundary, but not for an absolute claim that no undocumented behavior exists. I therefore use “not verified” for gaps, label local tests and architectural inferences, and avoid treating a vendor's feature ranking as an independent comparison.

## Sources and further reading

**Server-style managers**
- OpenBao: [homepage](https://openbao.org/) · [audit devices](https://openbao.org/docs/audit/) · [file audit device](https://openbao.org/docs/audit/file/) · [filesystem storage](https://openbao.org/docs/configuration/storage/filesystem/) · [declarative configuration](https://openbao.org/blog/features-declarative-configuration/) · [self-initialization](https://openbao.org/docs/configuration/self-init/) · [dev server warning](https://openbao.org/docs/concepts/dev-server/) · [Homebrew formula](https://formulae.brew.sh/formula/openbao)
- HashiCorp: [BUSL announcement](https://www.hashicorp.com/en/blog/hashicorp-adopts-business-source-license) · [Vault LICENSE](https://github.com/hashicorp/vault/blob/main/LICENSE) · [Vault MCP server docs](https://developer.hashicorp.com/vault/docs/mcp-server/overview) · [HashiConf 2025 announcement](https://www.hashicorp.com/en/blog/strengthen-security-with-vault-boundary-and-radar-features-at-hashiconf-2025)
- IBM: [acquisition completion](https://newsroom.ibm.com/2025-02-27-ibm-completes-acquisition-of-hashicorp,-creates-comprehensive,-end-to-end-hybrid-cloud-platform)
- Infisical: [docker-compose deployment](https://infisical.com/docs/self-hosting/deployment-options/docker-compose) · [audit logs](https://infisical.com/docs/documentation/platform/audit-logs) · [repo/license](https://github.com/Infisical/infisical)
- CyberArk Conjur: [releases](https://github.com/cyberark/conjur/releases) · [OSS audit-support answer](https://discuss.cyberarkcommons.org/t/can-i-get-audit-logs-via-rest-api/1331/2) · Square Keywhiz: [archived repo](https://github.com/square/keywhiz)

**Password-manager vaults**
- KeePassXC: [keepassxc-cli man page](https://man.archlinux.org/man/keepassxc-cli.1.en) · [User Guide (Secret Service)](https://keepassxc.org/docs/KeePassXC_UserGuide.html)
- Bitwarden: [CLI](https://bitwarden.com/help/cli/) · [event logs](https://bitwarden.com/help/event-logs/) · [Secrets Manager self-hosting](https://bitwarden.com/blog/enterprise-self-hosting-for-bitwarden-secrets-manager/)
- Vaultwarden: [repo](https://github.com/dani-garcia/vaultwarden) · [events discussion](https://github.com/dani-garcia/vaultwarden/discussions/3545) · [Secrets Manager discussion](https://github.com/dani-garcia/vaultwarden/discussions/5702)
- 1Password: [1Password 8 membership requirement](https://support.1password.com/migrate-1password-account/) · [Connect](https://www.1password.dev/connect/) · [Environments MCP server](https://www.1password.dev/environments/mcp-server) · [MCP security blog](https://1password.com/blog/securing-mcp-servers-with-1password-stop-credential-exposure-in-your-agent)
- Psono: [audit log docs](https://doc.psono.com/admin/configuration/audit-log.html) · [psonoci](https://github.com/meldron/psonoci) · Passbolt: [pricing](https://www.passbolt.com/pricing) · [file-attachment request](https://community.passbolt.com/c/backlog/6) · gopass: [features](https://github.com/gopasspw/gopass/blob/master/docs/features.md)

**Injectors**
- SecretSpec: [repo](https://github.com/cachix/secretspec) · [announcement](https://devenv.sh/blog/2025/07/21/announcing-secretspec-declarative-secrets-management)
- novops: [repo](https://github.com/PierreBeucher/novops) · dotenvx: [repo](https://github.com/dotenvx/dotenvx) · fnox: [repo](https://github.com/jdx/fnox) · mise: [secrets docs](https://mise.jdx.dev/environments/secrets/) · vals: [repo](https://github.com/helmfile/vals)
- envchain: [repo](https://github.com/sorah/envchain) · aws-vault: [abandoned upstream](https://github.com/99designs/aws-vault) · [ByteNess fork](https://github.com/ByteNess/aws-vault) · chamber: [repo](https://github.com/segmentio/chamber) · teller: [releases](https://github.com/tellerops/teller/releases)
- age: [Homebrew formula](https://formulae.brew.sh/formula/age) · age-plugin-se: [repo](https://github.com/remko/age-plugin-se)

**Agent-era & MCP**
- Pomerium: [MCP capability](https://www.pomerium.com/docs/capabilities/mcp)
- Frank Denis: [Leaky MCP servers](https://00f.net/2025/06/16/leaky-mcp-servers/)
- GitGuardian: [State of Secrets Sprawl 2026](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/)
- OWASP: [MCP01:2025 Token Mismanagement](https://owasp.org/www-project-mcp-top-10/2025/MCP01-2025-Token-Mismanagement-and-Secret-Exposure)
- Claude Code: [authentication](https://code.claude.com/docs/en/iam) · [settings](https://code.claude.com/docs/en/settings) · [sandboxing](https://code.claude.com/docs/en/sandboxing) · [Keychain 4096-byte issue](https://github.com/anthropics/claude-code/issues/28901)

**macOS primitives**
- Apple: [unified logging](https://developer.apple.com/documentation/os/logging) · [log rotation categories](https://developer.apple.com/documentation/oslog/oslogentrystorecategory) · [BSD file flags](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemDetails/FileSystemDetails.html) · [FileVault behavior](https://developer.apple.com/library/archive/documentation/Security/Conceptual/Security_Overview/CryptographicServices/CryptographicServices.html)
- [eslogger man page](https://keith.github.io/xcode-man-pages/eslogger.1.html) · [Objective-See FileMonitor](https://objective-see.org/products/utilities.html) · [Santa FAA](https://northpole.dev/features/faa/) · [Santa telemetry](https://northpole.dev/features/telemetry/) · [Eclectic Light on vanishing keychain logs](https://eclecticlight.co/2017/11/26/last-week-on-my-mac-vanishing-keychains/) · [auditd man page](https://keith.github.io/xcode-man-pages/auditd.8.html)
