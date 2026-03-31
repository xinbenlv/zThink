---
title: "Security Analysis of Claude Code v2.1.88 — Source Reconstructed from Source Maps"
excerpt: "A deep-dive security review of Claude Code's internals, reconstructed from its published source maps. Covers permission sandboxing, shell execution, credential handling, remote killswitches, and 10 findings."
date: 2026-03-31
lang: en
categories:
  - blog
tags:
  - security
  - claude-code
  - anthropic
  - static-analysis
---

# Security Analysis Report: Claude Code v2.1.88

**Date:** 2026-03-31
**Source:** Reconstructed from `cli.js.map` (source map) in `@anthropic-ai/claude-code@2.1.88`
**Total source files:** 4,756 (1,902 under `src/`, rest are `node_modules/` and `vendor/`)
**Method:** Static code review of extracted TypeScript/TSX source

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Architecture Overview](#2-architecture-overview)
3. [Secrets & Credential Handling](#3-secrets--credential-handling)
4. [Authentication & Authorization](#4-authentication--authorization)
5. [Permission Model & Sandbox](#5-permission-model--sandbox)
6. [Remote Feature Gates (GrowthBook/Statsig)](#6-remote-feature-gates-growthbookstatsig)
7. [Bash / Shell Execution Security](#7-bash--shell-execution-security)
8. [Path Traversal & Filesystem Protection](#8-path-traversal--filesystem-protection)
9. [Network Security (WebFetch)](#9-network-security-webfetch)
10. [Code Injection Analysis](#10-code-injection-analysis)
11. [Prompt Injection & Data Leakage](#11-prompt-injection--data-leakage)
12. [Supply Chain Security](#12-supply-chain-security)
13. [Internal / "Ant-Only" Features](#13-internal--ant-only-features)
14. [Findings Summary Table](#14-findings-summary-table)
15. [Recommendations](#15-recommendations)

---

## 1. Executive Summary

Claude Code v2.1.88 demonstrates a **mature, defense-in-depth security architecture**. The codebase uses multi-stage validation for shell commands, comprehensive path sanitization, PKCE-based OAuth, OS keychain credential storage, and a layered permission system with remote killswitch capability.

**No critical vulnerabilities were found.** The most notable concerns are:

- A `bypassPermissions` mode that disables all permission checks (mitigated by a remote killswitch)
- Dangerous shell pattern blocking that is partially restricted to internal ("ant") users only
- Tree-sitter bash parser fallback to less robust regex analysis in external builds
- A 5-minute cache TTL for domain safety checks, allowing brief windows after domain compromise

**Overall risk assessment: LOW**

---

## 2. Architecture Overview

### Security Decision Flow

```
User Input / AI Tool Call
        │
        ▼
┌─────────────────────┐
│  Permission System   │  ← Rules: deny → ask → allow → default(ask)
│  (permissions.ts)    │  ← Remote gates (GrowthBook/Statsig)
└────────┬────────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌────────┐ ┌────────────┐
│  Bash  │ │ File Tools │
│  Tool  │ │ Read/Write │
└───┬────┘ └─────┬──────┘
    │            │
    ▼            ▼
┌────────────┐ ┌──────────────────┐
│ Multi-stage│ │ Path validation  │
│ parse →    │ │ Traversal check  │
│ detect →   │ │ Dangerous files  │
│ semantic → │ │ Symlink protect  │
│ permission │ │ Case-insensitive │
└────────────┘ └──────────────────┘
```

### Key Components

| Component | Path | Purpose |
|-----------|------|---------|
| Permission engine | `utils/permissions/` | Multi-mode permission system with rule matching |
| Bash security | `utils/bash/bashSecurity.ts`, `ast.ts`, `commands.ts` | Multi-stage command validation |
| Shell execution | `utils/Shell.ts` | Process spawning with sandbox wrapping |
| Credential storage | `utils/secureStorage/` | macOS Keychain + plaintext fallback |
| WebFetch | `tools/WebFetchTool/` | URL validation, SSRF protection, domain blocking |
| Feature gates | `services/analytics/growthbook.ts` | Remote killswitches via GrowthBook/Statsig |
| Subprocess scrubbing | `utils/subprocessEnv.ts` | Strip secrets from child process environments |
| Undercover mode | `utils/undercover.ts` | Prevent internal codename leakage |

---

## 3. Secrets & Credential Handling

### 3.1 Secure Storage

**Primary: macOS Keychain** (`utils/secureStorage/macOsKeychainStorage.ts`)
- Credentials stored in macOS Keychain using hex encoding
- Hex encoding prevents credential visibility in process monitors (addresses CrowdStrike detection concerns noted in comments)

**Fallback: Plaintext File** (`utils/secureStorage/plainTextStorage.ts`)
- Stores credentials in `~/.claude/.credentials.json`
- File permissions set to `0o600` (owner read/write only) at line 61
- Explicit warning returned to user: `"Warning: Storing credentials in plaintext."` (line 64)
- Used only when OS keychain is unavailable

### 3.2 API Key Handling

- `ANTHROPIC_API_KEY` retrieved via centralized `getAnthropicApiKey()` function
- Keys are never logged directly — auth status logged as booleans: `has Authorization header: ${!!customHeaders['Authorization']}` (`services/api/client.ts:120`)
- API key display truncated in UI: `sk-ant-...{last chars}` (`components/ApproveApiKey.tsx:63-71`)
- Keys normalized/hashed for config storage via `normalizeApiKeyForConfig()`

### 3.3 Subprocess Environment Scrubbing

**File:** `utils/subprocessEnv.ts`

When `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is enabled (automatically set in GitHub Actions with untrusted content), the following are stripped from child process environments:

| Category | Variables Stripped |
|----------|-------------------|
| Anthropic auth | `ANTHROPIC_API_KEY`, `CLAUDE_CODE_OAUTH_TOKEN`, `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_FOUNDRY_API_KEY`, `ANTHROPIC_CUSTOM_HEADERS` |
| OTEL headers | `OTEL_EXPORTER_OTLP_HEADERS`, `..._LOGS_HEADERS`, `..._METRICS_HEADERS`, `..._TRACES_HEADERS` |
| Cloud credentials | `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`, `AWS_BEARER_TOKEN_BEDROCK`, `GOOGLE_APPLICATION_CREDENTIALS`, `AZURE_CLIENT_SECRET`, `AZURE_CLIENT_CERTIFICATE_PATH` |
| GitHub Actions OIDC | `ACTIONS_ID_TOKEN_REQUEST_TOKEN`, `ACTIONS_ID_TOKEN_REQUEST_URL` |
| GitHub Actions runtime | `ACTIONS_RUNTIME_TOKEN`, `ACTIONS_RUNTIME_URL` |
| Action-specific | `ALL_INPUTS`, `OVERRIDE_GITHUB_TOKEN`, `DEFAULT_WORKFLOW_TOKEN`, `SSH_SIGNING_KEY` |

Also strips `INPUT_<NAME>` duplicates that GitHub Actions auto-creates for `with:` inputs.

**Note:** `GITHUB_TOKEN`/`GH_TOKEN` are intentionally **not** scrubbed — wrapper scripts need them, and they are job-scoped and expire when the workflow ends.

### 3.4 Client-Side Secret Scanning

**File:** `services/teamMemorySync/secretScanner.ts`

Before uploading to team memory, a secret scanner with 40+ gitleaks-based rules checks for:
- Anthropic API keys (`sk-ant-*` pattern)
- AWS, GCP, Azure credentials
- GitHub PATs, Slack tokens, etc.

Detected secrets are replaced with `[REDACTED]` before storage.

---

## 4. Authentication & Authorization

### 4.1 OAuth Implementation

**File:** `services/oauth/client.ts`

- Uses **PKCE** (Proof Key for Code Exchange) flow with `code_challenge` and `code_verifier`
- OAuth parameters redacted from logs via `redactSensitiveUrlParams()` in `services/mcp/auth.ts:100-125` — strips `state`, `nonce`, `code_challenge`, `code_verifier`, `code`
- Token refresh with proper scoping
- CSRF protection via `state` and `nonce` parameters

### 4.2 Supported Auth Methods

**File:** `services/api/client.ts`

| Provider | Mechanism |
|----------|-----------|
| Anthropic Direct | `x-api-key` header |
| OAuth | `Authorization: Bearer` token |
| AWS Bedrock | `AWS_BEARER_TOKEN_BEDROCK` |
| Azure Foundry | Azure client credentials |
| GCP Vertex AI | Google application credentials |

### 4.3 MCP Server Authentication

**File:** `services/mcp/auth.ts`

- Implements OAuth discovery per RFC 9728 & RFC 8414
- Token caching and refresh
- Error normalization for non-standard OAuth servers (e.g., Slack)
- Authorization server metadata discovery

### 4.4 MCP Header Helpers

**File:** `services/mcp/headersHelper.ts`

- Dynamic headers can be fetched from helper scripts
- Trust dialog validation required before executing `headersHelper` from project/local settings (lines 20-56)
- Output validated: must be a JSON object with string-only values (lines 79-97)

---

## 5. Permission Model & Sandbox

### 5.1 Permission Modes

**File:** `utils/permissions/PermissionMode.ts`

| Mode | Behavior | Color |
|------|----------|-------|
| `default` | Ask user for each tool use | Normal |
| `plan` | Plan mode with approval required | Blue |
| `acceptEdits` | Auto-approve file edits within working directory | Green |
| `bypassPermissions` | **Skip ALL permission checks** | **Red** |
| `dontAsk` | Auto-deny without prompting | Red |
| `auto` | ML classifier-based auto-approval (ant-only, requires `TRANSCRIPT_CLASSIFIER` feature flag) | Yellow |

### 5.2 Permission Rule System

**Files:** `utils/permissions/PermissionRule.ts`, `permissionRuleParser.ts`

Rules are parsed into **Tool + RuleContent + Behavior** triplets:
- Rules evaluated in order: **deny → ask → allow**
- Prefix matching for patterns like `Bash(python:*)`, `PowerShell(rm:*)`
- Wildcard patterns for complex cases
- Rule sources: config file, CLI flags, session, or slash commands

### 5.3 Dangerous Pattern Stripping in Auto Mode

**File:** `utils/permissions/permissionSetup.ts:94-147`

When entering auto mode, rules matching dangerous interpreters are automatically stripped. The matcher handles variants: exact match, `:*`, `*`, ` *`, ` -*`.

This prevents rules like `Bash(python:*)` from auto-allowing arbitrary code execution in auto mode.

### 5.4 Dangerous Shell Patterns

**File:** `utils/permissions/dangerousPatterns.ts`

**Cross-platform (all users):**
```
python, python3, python2, node, deno, tsx, ruby, perl, php, lua,
npx, bunx, npm run, yarn run, pnpm run, bun run,
bash, sh, ssh
```

**Additional patterns (ant-only, lines 58-79):**
```
zsh, fish, eval, exec, env, xargs, sudo,
fa run, coo, gh, gh api, curl, wget, git, kubectl, aws, gcloud, gsutil
```

> **Finding:** External users do not get protection against auto-allowing `curl`, `wget`, `git`, `gh`, `kubectl`, `aws`, `gcloud`, etc. These are only blocked for internal Anthropic users. See [Finding #2](#14-findings-summary-table).

### 5.5 bypassPermissions Mode

**File:** `utils/permissions/PermissionMode.ts:66-71`

This mode completely disables all permission checks. It is:
- Shown in red (`color: 'error'`) as a visual danger indicator
- Controlled by a remote killswitch (see Section 6)
- Activated via `--dangerously-skip-permissions` CLI flag

### 5.6 Filesystem Permission Controls

**File:** `utils/permissions/filesystem.ts`

**Protected files (auto-edit blocked):**
```
.gitconfig, .gitmodules, .bashrc, .bash_profile,
.zshrc, .zprofile, .profile, .ripgreprc, .mcp.json, .claude.json
```

**Protected directories:**
```
.git, .vscode, .idea, .claude
```

- Case-insensitive path comparison prevents bypass via mixed-case paths on macOS/Windows (e.g., `.cLauDe/Settings.locaL.json`)
- Skill scope validation with traversal checks and glob metacharacter rejection

---

## 6. Remote Feature Gates (GrowthBook/Statsig)

### 6.1 Architecture

**File:** `services/analytics/growthbook.ts`

Claude Code uses **GrowthBook** (a feature flagging/A/B testing platform) and **Statsig** for remote configuration. These control:

- `tengu_disable_bypass_permissions_mode` — killswitch for bypassPermissions mode
- `TRANSCRIPT_CLASSIFIER` — gates the auto mode ML classifier
- Various other feature flags for security and functionality

### 6.2 bypassPermissions Killswitch

**File:** `utils/permissions/bypassPermissionsKillswitch.ts`

The flow:

1. User opts into `bypassPermissions` mode locally
2. Before the first query, Claude Code calls `shouldDisableBypassPermissions()`
3. This checks the `tengu_disable_bypass_permissions_mode` gate via GrowthBook
4. If gate returns `true` → the client **forcibly downgrades** the user out of bypass mode
5. If gate returns `false` or is unreachable → bypass mode stays as user set it

**Key properties:**
- **One-way only:** Anthropic can **revoke** bypassPermissions remotely, but cannot **grant** it — the user must opt in locally
- **Fail-open:** If GrowthBook is unreachable, defaults to `false` (don't disable) — see `growthbook.ts:887-888`: `// No cache - return false (don't block on init for uncached gates)`
- **Runs once:** Only checks before the first query per session (`bypassPermissionsCheckRan` flag)
- **Resets on login:** `resetBypassPermissionsCheck()` re-runs the check after `/login` to pick up new org context

**Override chain** (`checkSecurityRestrictionGate`, lines 854-862):
1. Environment variable overrides (for eval harnesses)
2. Config file overrides
3. Statsig cache (safety fallback from previous session)
4. GrowthBook cache
5. Default: `false`

### 6.3 Auto Mode Gate

**File:** `utils/permissions/bypassPermissionsKillswitch.ts:74-117`

Similar pattern for auto mode:
- Gated on `TRANSCRIPT_CLASSIFIER` feature flag (build-time)
- Runtime gate via `verifyAutoModeGateAccess()` with GrowthBook
- Re-checks when model or fast mode changes
- Can display notification warnings to user

---

## 7. Bash / Shell Execution Security

### 7.1 Multi-Stage Validation Pipeline

```
Command Input
      │
      ▼
┌─────────────────────────────┐
│ Stage 1: AST Parsing        │  tree-sitter-bash (preferred)
│ (ast.ts, parser.ts)         │  or shell-quote + regex (fallback)
├─────────────────────────────┤
│ Stage 2: Dangerous Patterns │  23+ security checks
│ (bashSecurity.ts)           │  Zsh-specific bypass detection
├─────────────────────────────┤
│ Stage 3: Semantic Analysis  │  Redirect validation
│ (commands.ts)               │  Environment variable tracking
├─────────────────────────────┤
│ Stage 4: Permission Match   │  argv[0] + subcommands vs rules
│ (bashPermissions.ts)        │  Wrapper handling (timeout, nohup)
└─────────────────────────────┘
```

### 7.2 AST Parsing (Stage 1)

**File:** `utils/bash/ast.ts`, `utils/bash/parser.ts`

- **Primary:** tree-sitter-bash parser for full AST analysis
- **Fallback:** shell-quote library + regex (external builds where tree-sitter is unavailable)
- **Fail-closed:** `PARSE_ABORTED` sentinel (line 93) distinguishes timeout/panic from successful null parse
- Allowlist of safe AST node types; anything not explicitly handled becomes `too-complex` (requiring user approval)
- Conservative variable assignment tracking and resolution

> **Finding:** The tree-sitter fallback path is less robust. External builds using regex-based parsing are more susceptible to parser differential attacks. See [Finding #3](#14-findings-summary-table).

### 7.3 Dangerous Pattern Detection (Stage 2)

**File:** `utils/bash/bashSecurity.ts`

23+ security checks (`BASH_SECURITY_CHECK_IDS`, lines 76-101) including:

- Command substitution (`$(...)`, `` `...` ``)
- Process substitution (`<(...)`, `>(...)`)
- IFS injection
- Control characters
- Unicode whitespace (U+00A0, U+2000-U+200B, etc.)
- Brace expansion with quotes
- Heredoc extraction

**Zsh-specific bypass detection (lines 22-73):**
- Zsh equals expansion: `=cmd` → `/usr/bin/cmd`
- Zsh process substitution: `=(cmd)`
- Zsh module loading: `zmodload`, `zpty`, `ztcp`
- PowerShell comment syntax: `<#`

### 7.4 Shell Quoting Security

**File:** `utils/bash/shellQuote.ts`

- Safe wrapper around `shell-quote` library with error handling
- Strict input type validation (lines 47-95)
- Detects malformed tokens and unterminated quotes (lines 117-143)
- **Cryptographic placeholder salt:** 8 random bytes in hex (lines 20-36) prevent injection attacks like `sort __SINGLE_QUOTE__ hello --help`
- Checks for unbalanced braces/parentheses

### 7.5 Command Continuation Handling

**File:** `utils/bash/commands.ts:106-139`

- Correctly handles `\<newline>` line continuations with odd/even backslash counting
- Prevents exploits like `tr\<NL>aceroute` being parsed as two commands
- Heredocs extracted before parsing and restored after, to work around shell-quote limitations

### 7.6 Output Redirection Security

**File:** `utils/bash/commands.ts:42-81`

- Only static redirections to `/dev/null` and stderr-to-stdout pipes are stripped
- Dynamic targets (variables, command substitutions, globs, tilde expansion) are rejected and require user approval

### 7.7 Shell Providers

**Bash** (`utils/shell/bashProvider.ts`):
- Disables extglob patterns (line 45)
- Commands wrapped with `eval` for alias expansion
- Safe `pwd -P >| quoted_path` redirection

**PowerShell** (`utils/shell/powershellProvider.ts`):
- Uses `-EncodedCommand` with base64 UTF-16LE encoding instead of `-Command`
- Per-cmdlet parameter validation
- Cmdlet-specific path parameter tracking (`tools/PowerShellTool/pathValidation.ts`)

### 7.8 Process Spawning

**File:** `utils/Shell.ts`

- Uses `spawn()` with **separate args array** (never shell string concatenation)
- Commands passed to shell via `-c` argument with proper quoting
- Never uses `shell: true` with unsanitized user input
- `O_NOFOLLOW` flag prevents symlink attacks (line 303)
- Sandbox wrapping for additional isolation

---

## 8. Path Traversal & Filesystem Protection

### 8.1 Path Validation

**File:** `utils/path.ts`

| Check | Implementation |
|-------|---------------|
| Type validation | `typeof path !== 'string'` throws TypeError (lines 37-45) |
| Null byte detection | `path.includes('\0')` throws Error (lines 48-50) |
| Tilde expansion | Safe `~/` handling via `homedir()` (lines 59-65) |
| Traversal detection | Regex `/(?:^\|[\\/])\.\.(?:[\\/]\|$)/` matches `../` patterns |
| UNC path blocking | Skip filesystem ops for `\\` and `//` paths — prevents NTLM credential leak attacks |
| Windows path conversion | POSIX-style `/c/Users/...` → `C:\Users\...` on Windows |
| Unicode normalization | All paths normalized to NFC form |

### 8.2 File Read Tool Protection

**File:** `tools/FileReadTool/FileReadTool.ts`

Blocks dangerous device paths (lines 98-128):
- `/dev/zero`, `/dev/urandom`, `/dev/tty` (prevents hangs)
- `/proc/*/fd/0-2` (stdin/stdout/stderr aliases)
- Validates against readability permissions

### 8.3 File Write Tool Protection

**File:** `tools/FileWriteTool/FileWriteTool.ts`

- Path expansion in `backfillObservableInput()` (lines 125-130)
- Wildcard pattern matching for permissions (line 133)
- Write permission checks via `checkWritePermissionForTool()` (line 137)

---

## 9. Network Security (WebFetch)

### 9.1 URL Validation

**File:** `tools/WebFetchTool/utils.ts`

| Control | Detail |
|---------|--------|
| Max URL length | 2,000 characters (line 106) |
| Max HTTP content | 10 MB (line 112) |
| Fetch timeout | 60 seconds (line 116) |
| Max redirects | 10 hops (line 125) |
| Credential blocking | URLs with embedded `username:password` rejected (lines 156-158) |
| Single-label hostname blocking | Requires at least 2 domain parts (line 164) — prevents internal network access |
| HTTP → HTTPS upgrade | Automatic at lines 376-377 |
| Markdown truncation | 100,000 characters max (line 128) |

### 9.2 Redirect Security

**File:** `tools/WebFetchTool/utils.ts:212-243`

- Only allows **same-origin** redirects (with optional `www.` variations)
- Validates protocol, port, and credentials match on redirects
- Cross-domain redirects require user approval
- 10-hop cap prevents redirect loop DoS

### 9.3 Domain Blocklist Preflight

**File:** `tools/WebFetchTool/utils.ts:176-203`

- Queries `api.anthropic.com/api/web/domain_info` before fetching
- 10-second timeout for the check
- Results cached with 5-minute TTL in LRU cache
- URL content cached with 15-minute TTL

> **Finding:** The 5-minute cache TTL means a newly-compromised domain could remain accessible for up to 5 minutes after being blocklisted. See [Finding #4](#14-findings-summary-table).

### 9.4 Preapproved Domains

**File:** `tools/WebFetchTool/preapproved.ts`

130+ curated domains for documentation and package registries are preapproved for GET-only WebFetch access. These bypass the domain blocklist check.

**Security separation** (explicitly documented in comments, lines 5-12):
- Preapproved list is **only for WebFetch** (GET requests)
- **Not** inherited by the sandbox system for general network restrictions
- Some preapproved domains (e.g., `huggingface.co`, `kaggle.com`, `nuget.org`) allow file uploads and would be dangerous for unrestricted access

Path-prefixed entries validated with segment boundaries (line 162):
```typescript
if (pathname === p || pathname.startsWith(p + '/')) return true
```
This prevents `/anthropics` from matching `/anthropics-evil/malware`.

### 9.5 Missing Protocol Check

The URL validation function (`validateURL`) does not explicitly check for `file://` protocol. While `new URL('file:///etc/passwd')` would have a hostname of `""` (empty string) and `parts.length < 2` would catch `""`, this is an implicit rather than explicit check.

---

## 10. Code Injection Analysis

### 10.1 Dynamic Code Execution

| Pattern | Found | Status |
|---------|-------|--------|
| `eval()` | 0 | Safe |
| `new Function()` | 0 | Safe |
| `vm.runInContext()` | 0 | Safe |
| `vm.runInNewContext()` | 0 | Safe |
| `vm.runInThisContext()` | 0 | Safe |

**No dynamic code execution patterns found in the codebase.**

### 10.2 Module Loading

- 30 files with `require`/dynamic `import` — all legitimate module loading
- MCP feature loading uses conditional require gated by feature flags:
  ```typescript
  const fetchMcpSkillsForClient = feature('MCP_SKILLS')
    ? (require('../../skills/mcpSkills.js') as ...)
    : null
  ```
- No dynamic requires with user-controlled paths

### 10.3 JSON Parsing

- 53+ JSON operations found — all use standard `JSON.parse()`/`JSON.stringify()`
- Schema validation via Zod library (`z.object`, `z.string`, etc.)
- No `eval()` of JSON data

---

## 11. Prompt Injection & Data Leakage

### 11.1 WebFetch Output Processing

**File:** `tools/WebFetchTool/utils.ts`, `WebFetchTool.ts`

- HTML converted to Markdown via Turndown library
- Markdown output passed to Claude for summarization via `applyPromptToMarkdown()`
- Output cached in LRU cache

> **Finding:** No explicit HTML sanitization before Markdown conversion. A crafted web page could inject Markdown that formats in unexpected ways. See [Finding #5](#14-findings-summary-table).

### 11.2 Bash Tool Output

- Tool output (command results) are **not** used to make security decisions
- Security decisions based solely on **command text**, not output
- This is correct — output injection cannot bypass the sandbox

### 11.3 Analytics Data Sanitization

**File:** `services/analytics/metadata.ts`

- Sensitive marker type `AnalyticsMetadata_I_VERIFIED_THIS_IS_NOT_CODE_OR_FILEPATHS` forces explicit verification that logged data doesn't contain code/file paths
- MCP tool names redacted as `'mcp_tool'` by default (lines 70-77)
- Custom MCPs sanitized while official registry MCPs can be logged (lines 102-116)

### 11.4 OAuth Parameter Redaction

**File:** `services/mcp/auth.ts:100-125`

`redactSensitiveUrlParams()` strips OAuth parameters from logs:
- `state`, `nonce`, `code_challenge`, `code_verifier`, `code`

### 11.5 Undercover Mode

**File:** `utils/undercover.ts`

Prevents Anthropic-internal information leakage when contributing to public repositories:

- **Activation:** Auto-enabled unless repo remote matches internal allowlist; force-on via `CLAUDE_CODE_UNDERCOVER=1`; **no force-off** (safety default)
- **Scope:** Only active for `USER_TYPE === 'ant'` (internal builds); dead-code-eliminated in external builds
- **Blocks in commits/PRs:** Internal model codenames (Capybara, Tengu, etc.), unreleased model versions, internal repo names, Slack channels, short links, "Claude Code" attribution, Co-Authored-By lines

### 11.6 Error Message Safety

**File:** `services/api/errors.ts`

- Error messages are generic and helpful (e.g., `"Not logged in · Please run /login"`)
- No API keys or token values included in error messages

---

## 12. Supply Chain Security

### 12.1 Dependencies

The published `package.json` has minimal explicit dependencies. The application is bundled into a single `cli.js` (13 MB) with an accompanying source map (59.8 MB).

### 12.2 No Suspicious Patterns

- No postinstall/preinstall scripts in package.json
- No dynamic requires from external sources in core security modules
- MCP plugin loading uses explicit path resolution, not arbitrary URL fetching

### 12.3 Hook System

**File:** `utils/hooks.ts`

- User-defined shell hooks executed via `spawn()` (line 7)
- Hooks sourced from user configuration files
- Input validation through `HookCallback` type schema (lines 66-74)
- Hook execution gated on permission system

### 12.4 Plugin Loading

**File:** `utils/plugins/pluginLoader.ts`

- Plugin path sanitization (removes non-alphanumeric characters, lines 145-150)
- Marketplace policy enforcement via `isSourceAllowedByPolicy()`, `isSourceInBlocklist()`
- Manifest validation with schemas
- Git repository cloning with controlled commands

---

## 13. Internal / "Ant-Only" Features

Several security features are gated on `process.env.USER_TYPE === 'ant'`, which is a **build-time define** (constant-folded by the bundler):

| Feature | Behavior for External Users |
|---------|---------------------------|
| Extended dangerous patterns (curl, git, gh, kubectl, aws, gcloud, gsutil) | **Not blocked** — only basic interpreter patterns protected |
| Auto mode (ML classifier) | Unavailable — gated on `TRANSCRIPT_CLASSIFIER` |
| Undercover mode | Dead-code-eliminated — all functions return trivially |
| Additional zsh/fish/eval/exec/env/xargs/sudo patterns | Available to all users (in `DANGEROUS_BASH_PATTERNS` before the ant-only block) |

The ant-only gating is documented in `dangerousPatterns.ts:53-57`:
> "These stay ant-only — external users don't have coo, and the rest are an empirical-risk call grounded in ant sandbox data, not a universal 'this tool is unsafe' judgment."

---

## 14. Findings Summary Table

| # | Severity | Finding | Location | Mitigation |
|---|----------|---------|----------|------------|
| 1 | **High** | `bypassPermissions` mode disables ALL permission checks | `PermissionMode.ts:66-71` | Remote killswitch via GrowthBook gate `tengu_disable_bypass_permissions_mode`; requires explicit `--dangerously-skip-permissions` flag; Anthropic can revoke remotely but cannot grant; killswitch is **fail-open** (if GrowthBook unreachable, bypass stays) |
| 2 | **High** | Dangerous shell patterns (curl, wget, git, gh, kubectl, aws, gcloud) only blocked for internal ant users | `dangerousPatterns.ts:58-79` | Basic interpreter blocking (python, node, ruby, etc.) applies to all users; ant-only patterns based on internal usage data |
| 3 | **Medium** | Tree-sitter bash parser fallback to less robust regex in external builds | `parser.ts:65-83` | Fail-closed design — unknown syntax becomes `too-complex` requiring user approval; extensive regex checks as secondary layer |
| 4 | **Medium** | Domain blocklist check cached for 5 minutes | `WebFetchTool/utils.ts:66-78` | Domain approval still requires user consent for non-preapproved domains |
| 5 | **Medium** | No HTML sanitization before Markdown conversion in WebFetch | `WebFetchTool/utils.ts:95` | Output is passed to Claude for summarization, not rendered directly; Markdown length capped at 100K chars |
| 6 | **Medium** | Excluded commands are user convenience, not a security boundary | `shouldUseSandbox.ts:18-20` | Explicitly documented as not a security boundary; permission system is the real enforcement layer |
| 7 | **Low** | Plaintext credential fallback when OS keychain unavailable | `plainTextStorage.ts:61-64` | 0o600 file permissions; explicit warning to user; only used when keychain fails |
| 8 | **Low** | No explicit `file://` protocol check in WebFetch URL validation | `WebFetchTool/utils.ts:139-168` | Implicitly blocked: `file://` URLs have empty hostname, caught by `parts.length < 2` check |
| 9 | **Low** | Preapproved domains (130+) bypass domain blocklist entirely | `preapproved.ts:5-12` | Curated list of documentation/registry domains; GET-only; path segment boundary enforcement; sandbox does NOT inherit this list |
| 10 | **Info** | Permission rule ordering could allow early `allow` to shadow later `deny` | `permissions.ts:126-173` | Rules processed deny → ask → allow; source ordering generally prevents this |

---

## 15. Recommendations

### Priority 1 (High)

1. **Extend dangerous pattern blocking to external users** — The ant-only gate on `curl`, `wget`, `git`, `gh`, `kubectl`, `aws`, `gcloud` leaves external users without auto-mode protection for these high-risk commands. Even if the current justification is based on internal usage data, these commands represent universal data exfiltration and code execution risks.

2. **Consider fail-closed behavior for bypassPermissions killswitch** — The current `checkSecurityRestrictionGate` returns `false` when GrowthBook is unreachable (`growthbook.ts:887-888`), meaning the killswitch is fail-open. If the intent is a safety mechanism, consider defaulting to `true` (disable bypass) when the remote check fails.

### Priority 2 (Medium)

3. **Ensure tree-sitter is bundled in all builds** — Or significantly harden the regex fallback path. Parser differential attacks are a known risk when the security parser and the execution parser disagree.

4. **Reduce domain check cache TTL** — Consider reducing from 5 minutes to 1 minute, or implement a push-based revocation mechanism for emergency domain blocks.

5. **Add HTML sanitization in WebFetch pipeline** — Sanitize HTML before Turndown Markdown conversion to prevent formatting injection from crafted web pages.

### Priority 3 (Low)

6. **Add explicit `file://` protocol rejection** — While implicitly blocked, an explicit check would be clearer and more robust against future refactoring.

7. **Consider requiring re-authentication for bypassPermissions** — Adding an MFA or re-auth step before enabling `--dangerously-skip-permissions` would add defense-in-depth.

8. **Document excluded commands limitation** — Ensure user-facing documentation clearly states that excluded commands are not a security boundary.

---

## Appendix: Security Architecture Strengths

The following security patterns are well-implemented and noteworthy:

- **Defense-in-depth for bash execution:** 4-stage validation pipeline with fail-closed defaults
- **Cryptographic placeholder salting:** Prevents injection via command parsing intermediaries
- **PKCE OAuth with parameter redaction:** Strong auth flow with no credential logging
- **Subprocess environment scrubbing:** Comprehensive secret stripping in CI/CD contexts
- **Case-insensitive path comparison:** Prevents filesystem case-folding bypasses on macOS/Windows
- **UNC path blocking:** Prevents NTLM credential leak attacks on Windows
- **Segment-boundary path matching:** Preapproved domain paths validated at `/` boundaries
- **Client-side secret scanning:** 40+ rules prevent credential upload to team memory
- **Undercover mode:** Automated prevention of internal information leakage to public repos
- **Remote killswitch capability:** Anthropic can remotely disable dangerous modes without shipping client updates
