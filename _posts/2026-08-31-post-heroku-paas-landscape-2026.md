---
title: "The Post-Heroku PaaS Landscape: A 2026 Guide for Your OPC (or Side Projects)"
excerpt: "Heroku isn't dead, but it's no longer the default. A 2026 field guide to Railway, Fly.io, Render, Heroku, and self-hosting — with real pricing math for running 10 to 100 small side projects."
date: 2026-08-31
lang: en
published: true
cover_image:
  src: /assets/blogposts/2026-08-31-post-heroku-paas-landscape-2026/post-heroku-paas-2026-00-cover.jpg
  x: 334
  y: 0
  size: 666
og_image: /assets/blogposts/2026-08-31-post-heroku-paas-landscape-2026/post-heroku-paas-2026-00-cover.jpg
categories:
  - blog
tags:
  - paas
  - railway
  - fly-io
  - render
  - heroku
  - self-hosted
  - devops
  - opc
---

## TL;DR

Heroku did not shut down — it is still fully operational, still Salesforce-owned, and its
pricing page is live today. What actually happened is narrower and more important for anyone
running a one-person company: Heroku lost its status as *the* default place to park a small
app for free, and the market that filled the vacuum split into three genuinely different
pricing philosophies. Which one is cheap for you depends entirely on the shape of your
portfolio — specifically, how many small, mostly-idle projects you run.

I run 16 small services, databases, and caches across 8 Railway projects today, for about
$17.57/month. That real account is the anchor for the math in this post: I project
what the same portfolio would cost at 10, 50, and 100 tiny projects on each pricing model. The
short version — usage-metered billing and self-hosting scale with what you actually use;
fixed-floor-per-service billing scales with how many projects you have, and that multiplies
badly once you're past a handful.

## Heroku isn't dead. It's just not the default anymore.

![A well-kept corner shop still open and lit at dusk, its free-sample tray empty and its chalkboard sign taken down](/assets/blogposts/2026-08-31-post-heroku-paas-landscape-2026/post-heroku-paas-2026-01-still-open.jpg)

Heroku is still running. [heroku.com/pricing](https://www.heroku.com/pricing/) is a live,
functioning checkout page today, sold under the "Heroku — from Salesforce" brand, with its own
[Salesforce status page](https://status.salesforce.com/products/Heroku). If you `git push
heroku main` right now, it will deploy. Nobody shut it down.

What actually happened is that Heroku stopped being the thing every tutorial told you to use
for a free side project. On [August 25, 2022, Heroku CEO Bob Wise announced](https://www.heroku.com/blog/next-chapter/#:~:text=Starting%20November%2028%2C%202022%2C%20we%20plan%20to%20stop%20offering%20free%20product%20plans) that,
starting **November 28, 2022**, Heroku would "stop offering free product plans" and begin
"shutting down free dynos and data services." Accounts inactive for a year would start losing
storage a month earlier, on October 26, 2022. That's the real event — not a shutdown, a
retirement of the free tier that had defined Heroku's identity since 2010.

Heroku's current [dyno and data-service pricing](https://www.heroku.com/pricing/) — behind
the "Show Cedar Dynos," "Show Fir Dynos," and "Show Postgres ... Plan Pricing" toggles on that
page — starts at $5/mo for a 0.5GB Eco dyno on its classic Cedar runtime, running up to
$1,500/mo for a 126GB Performance-2XL dyno; its newer, Kubernetes-based Fir dynos run $25 to
$2,400/mo. Postgres starts at $5/mo for a 1GB shared Essential-0 instance and scales, through
what the pricing page now buckets as "Classic" and "Advanced" tiers, up past $50,000/mo for
dedicated, high-availability, decoupled storage-and-compute configurations that no side
project will ever touch. Heroku is a completely viable, boring, well-run platform for a
production app with real revenue behind it. It is just no longer the reflexive answer to
"where do I put my weekend project for free,"
and that gap is what let the rest of this market fragment.

## Three pricing philosophies, one underlying question

![Three billing mechanisms on one workbench: a trickling brass usage meter, a row of coin-slot meters, and a self-built greenhouse frame with hand tools](/assets/blogposts/2026-08-31-post-heroku-paas-landscape-2026/post-heroku-paas-2026-02-three-meters.jpg)

Every PaaS that filled Heroku's vacated space picked one of three answers to the same
question: *what do you charge for, exactly?*

1. **Usage-metered, per-second billing.** You pay for CPU-seconds, memory-seconds, storage
   bytes, and egress actually consumed. An idle service costs close to zero because it isn't
   doing anything. Railway is the clearest example of this model; Fly.io behaves the same way
   for compute, as long as you aren't also paying for its fixed-price managed database
   product.
2. **Fixed per-service floor pricing.** Each service and each database has a minimum monthly
   dollar cost, independent of how idle it is — a $7/mo web service is $7/mo whether it serves
   one request a day or a million. Render and Heroku both work this way, and so does Fly.io's
   own *Managed Postgres* product, even though Fly.io's compute pricing is metered. The floor
   is the point: it buys operational simplicity and support in exchange for a price that does
   not shrink when your app is quiet.
3. **Self-hosted.** You rent raw compute — a VPS — and run an open-source PaaS layer like
   Coolify, Dokku, CapRover, or Dokploy on top of it to get back the git-push-to-deploy
   workflow. Cost scales with the size of the box, not with how many apps are crammed onto it,
   which makes it the cheapest option in raw dollars once you have enough tiny projects. The
   price you pay instead is operational: you now own backups, OS patching, TLS renewal, and
   uptime, and a single box going down takes every project on it down with it.

None of these is objectively "the good one." A single, always-busy production app with real
revenue is often cheapest on a fixed-floor platform, because the floor barely matters when the
service would cost more than that anyway. The philosophy that wins for an OPC running a dozen
tiny side projects — most of them serving a trickle of traffic most of the time — is a
different question entirely, and it's the one this post is built to answer.

## The anchor: what a real OPC portfolio actually costs today

![A shelf rack of small dormant pots and water jars all fed by a single copper pipe through one brass meter whose needle rests low](/assets/blogposts/2026-08-31-post-heroku-paas-landscape-2026/post-heroku-paas-2026-03-portfolio-shelf.jpg)

Rather than reason from vendor rate cards alone, I pulled my own account. I run 8 Railway
projects: 9 web/API services, 5 Postgres databases (153MB, 157MB, 198MB, 331MB, and 754MB —
all comfortably under 1GB), and 2 Redis instances (around 150MB each), fronting 8 live custom
domains. This is not a hypothetical OPC portfolio; it's the one I actually operate, a mix of
small internal tools, side projects, and a couple of things with real users.

For the current August 8 – September 8, 2026 billing cycle, Railway's own dashboard shows
$13.12 accrued so far, with a full-month estimate of **$17.57**, on the $5/mo Hobby plan (which
includes $5 of usage credit, so the effective floor before any usage-based billing kicks in is
$5/mo). The bill breaks down almost entirely by memory: $12.49 of that is the memory line item
alone, versus $0.30 for CPU, $0.11 for egress, $0.22 for volumes, and under a cent for backups.
Sixteen total compute resources — nine apps, five databases, two caches — for well under
$20/mo, because almost everything in that portfolio is idle almost all the time and idle time
on Railway costs close to nothing.

That's the whole argument in miniature. A platform that meters compute per second charges
roughly what you use. A platform with a fixed monthly floor per service charges you for
*owning* the service, whether or not anything is running on it. The rest of this post works
out what that difference does as the project count grows past 9.

(One aside on those 8 domains: Railway's own [pricing comparison table currently lists Hobby
as including 2 custom domains](https://railway.com/pricing#:~:text=Custom%20domains), yet my
Hobby-plan account runs 8 without any block or upsell prompt. Either the limit isn't enforced
in practice or it's stale documentation — I'd treat the number on the pricing page as directional
rather than a hard wall.)

## Philosophy 1: usage-metered, per-second billing

**Railway** is the purest expression of this model. Its [Hobby plan is $5/mo, which includes
$5 of usage credit](https://railway.com/pricing#:~:text=Hobby), so a portfolio that stays under
$5/mo of actual metered usage effectively costs $5/mo flat; beyond that, you're billed for
compute at roughly $0.00000772 per vCPU-second (about $20/vCPU-month if something ran at full
allocation nonstop) and $0.00000386 per GB-second of memory (about $10/GB-month at 100%
utilization), plus about $0.15/GB-month for volumes and $0.05/GB for egress. The key detail is
"per-second": a service that's asleep 23 hours a day and busy for one is billed for that one
hour, not for owning a slot on the platform. That's exactly why my own 16-resource, 8-project
account lands under $18/mo — almost everything in it is idle almost all the time.

**Fly.io** behaves the same way for compute. A `shared-cpu-1x` machine with 256MB of RAM runs
about [$1.94/mo](https://fly.io/docs/about/pricing/#:~:text=shared-cpu-1x) if left running
continuously, and Fly bills machines by the second, so a machine that spends most of its life
stopped costs closer to its storage price — [$0.15/GB-month for a stopped machine's
rootfs](https://fly.io/docs/about/pricing/#:~:text=Each%201GB%20of%20rootfs%20for%20a%20Machine%20stopped%20for%2030%20days%20is%20%240.15) — than its running price. The catch is the database: Fly's
metered pricing only applies to compute and storage you run yourself. If you self-host
Postgres as a Fly Machine with a volume, you stay inside this pricing philosophy. If you use
Fly's own managed database product instead, you leave it — see Philosophy 2.

## Philosophy 2: fixed per-service floor pricing

![A row of identical parking meters receding to the horizon, a coin dropped into every one, with every parking space beside them empty](/assets/blogposts/2026-08-31-post-heroku-paas-landscape-2026/post-heroku-paas-2026-04-meter-row.jpg)

**Heroku** is the platform this pricing model is most associated with, since it's the one that
trained a generation of developers on "one dyno, one price." Its cheapest always-on web
process is a $5/mo Eco dyno; its cheapest persistent Postgres is [$5/mo for a 1GB Essential-0
instance](https://www.heroku.com/pricing/) (behind the "Show Postgres Essential Plan Pricing"
toggle). Put one dyno and one database behind a real project and you're at a **minimum $10/mo
per project**, whether that project gets ten visitors a day or none.

**Render** runs the same philosophy with a cleaner workspace structure: the [Hobby workspace
itself is $0/mo](https://render.com/pricing#:~:text=Hobby) — the floor lives entirely at the
service level. A web service starts at [$7/mo for "less than 1 CPU" and 512MB of
RAM](https://render.com/pricing#:~:text=%247%2Fmonth), and Render does offer a genuinely free
Postgres tier, but it's explicitly [not meant for production — free databases expire 30 days
after creation](https://render.com/docs/free#:~:text=Do%20not%20use%20them%20for%20production%20applications) and are deleted after a grace period. The cheapest database you'd
actually trust with a real project is [$6/mo for 256MB](https://render.com/pricing#:~:text=%246%2Fmonth). One web service plus one small Postgres database on Render is a
**$13/mo floor per project** — and that's before egress past the included 5GB/mo, custom
domains past the 2 included on the Hobby workspace, or a Redis-compatible Key-Value store,
which itself starts at [$10/mo for 256MB](https://render.com/pricing#:~:text=%2410%2Fmonth).

**Fly.io's Managed Postgres (MPG)** is the case that makes the philosophy split visible inside
a single vendor. Fly's compute is metered, as covered above — but its managed database product
is not. MPG's cheapest tier, [Basic, is $38/mo for 1GB of storage on a shared-2x
instance](https://fly.io/docs/mpg/#:~:text=Basic), running up through Starter ($72/mo, 2GB),
Launch ($282/mo), Scale ($962/mo), and Performance ($1,922/mo), with additional storage priced
separately at [$0.28/GB-month](https://fly.io/docs/mpg/#:~:text=%240.28). A single MPG database
alone costs more per month than my entire 16-resource Railway account. That's not a knock on
MPG's engineering — it's a fully managed, HA-capable Postgres with automated backups and
failover, and for a database that actually needs that, $38/mo is reasonable. It's a knock on
using it under a portfolio of tiny, mostly-idle side projects, where you'd be paying enterprise
database rates for a database that holds a few hundred megabytes and gets queried a few times
an hour.

The shape is the same across all three: the floor buys you a fixed, predictable price and,
usually, more operational hand-holding — automated backups, one-click restores, a support
queue. What it does not do is get cheaper when the project underneath it is quiet.

## Philosophy 3: self-hosted

![A single lamplit greenhouse alone under a gathering storm, one person tending every shelf inside, fed by one power line and one pipe](/assets/blogposts/2026-08-31-post-heroku-paas-landscape-2026/post-heroku-paas-2026-05-one-greenhouse.jpg)

The third option skips the PaaS layer's pricing entirely: rent a VPS, put an open-source
deploy-and-manage layer on top of it, and get back roughly the Heroku experience — `git push`
to deploy, one-click databases, automatic TLS — on infrastructure you're renting by the box,
not by the service.

Four projects dominate this space, and I checked each directly against its GitHub repo rather
than the SEO round-ups that usually rank them (checked 2026-08-31):

- **[Coolify](https://github.com/coollabsio/coolify)** — 61,254 stars, Apache-2.0, launched
  2021. Manages servers, applications, and databases over a plain SSH connection, with over
  280 one-click services including Postgres and Redis, and native Docker Compose support. The
  most starred and most feature-complete of the four.
- **[Dokploy](https://github.com/Dokploy/dokploy)** — 37,002 stars, launched 2024, the newest
  and fastest-growing entrant. Native Docker Compose support plus multi-node scaling via Docker
  Swarm. One nuance worth knowing before you build on it: its license is Apache-2.0 for the
  core codebase, but a `/proprietary` directory carved out under a separate license covers some
  features — it isn't purely open source top to bottom the way Coolify and Dokku are.
- **[CapRover](https://github.com/caprover/caprover)** — 15,150 stars, the oldest of the four
  (created October 2017), built on Docker Swarm with Nginx for load balancing and Let's
  Encrypt for TLS. Its license is also a modified Apache-2.0 with a carve-out restricting
  redistribution of its paid features as a competing service — free to self-host and modify,
  but not unconditionally open.
- **[Dokku](https://github.com/dokku/dokku)** — 32,124 stars, MIT-licensed, the oldest project
  by far (2013) and the most Heroku-like of the set: it literally bills itself as a
  "docker-powered mini-Heroku" built on the same git-push-and-buildpack workflow, running one
  container per app rather than Coolify's or Dokploy's broader service catalog.

What none of these four give you is Railway's or Render's operations team. Backups, security
patching of the host OS, TLS certificate renewal, and uptime monitoring are yours. And because
every app on the box shares the same box, a single host failure — a bad kernel update, a
provider outage, a disk filling up — takes down every project running on it at once, not just
one. That's the trade you're making for a price curve that barely rises as you add tiny
projects: you've concentrated your operational risk exactly where you've minimized your cost.

The VPS underneath also matters, and it's a good example of why "just self-host it" is not a
permanently fixed price either. A 2 vCPU / 4GB machine — enough for a modest handful of tiny
services — costs [$0.0416/hr on AWS EC2 as a t3.medium in
us-east-1](https://instances.vantage.sh/aws/ec2/t3.medium#:~:text=starting%20at%20%240.0416%20per%20hour) and [$0.03350571/hr on GCP as an e2-medium in
us-central1](https://cloud.google.com/products/compute/pricing/general-purpose#:~:text=e2-medium) — **about $30.37/mo and $24.46/mo** respectively at a standard
730-hour month.
Budget-VPS providers like Hetzner are the reason self-hosting has a cost-per-project reputation
at all: the same 2 vCPU / 4GB shared-core box, [currently sold as the CX23 (Hetzner renamed it
from CX22 sometime after its June 2024 launch)](https://www.hetzner.com/cloud/cost-optimized/#:~:text=CX23), runs **€5.99/mo (about $7.09/mo)** — roughly a
quarter of the AWS price for the same specs. I'm flagging two things here that most self-hosting
round-ups gloss over. First, Hetzner's own pressroom confirms a [May 27, 2026 announcement of a
price increase effective June 15, 2026 that explicitly covers "all dedicated servers and cloud
plans at all locations,"](https://www.hetzner.com/pressroom/standardization-and-price-adjustment-of-our-server-products/#:~:text=All%20dedicated%20servers%20and%20cloud%20plans%20at%20all%20locations%20are%20affected%20by%20this%20adjustment) not just the dedicated-vCPU CPX line as some blog
aggregators claimed — the CX23's own listed launch price was [€3.79/mo in June
2024](https://www.hetzner.com/pressroom/new-cx-plans/#:~:text=%E2%82%AC%203.79), and it's up roughly 58% since then. Second, as of this writing
(August 31, 2026) the CX23 is marked **"not available" for new orders** on Hetzner's own site,
alongside its whole Cost-Optimized and Regular-Performance lines — worth checking current
availability before you build a plan around this exact SKU, though the dedicated-vCPU line
was unaffected and Hetzner routinely rotates SKUs in and out of availability.

## The payoff: 10, 50, 100 tiny projects, side by side

Here's the arithmetic, with the assumptions stated up front so you can redo it for your own
portfolio.

**Definition of "tiny project":** one small, mostly-idle web/API service plus one small
Postgres database — close to the actual 9-services-to-5-databases ratio in my own Railway
account, rounded to a clean 1:1 unit for easy math.

**What's a sourced price versus my own estimate:** every per-service and per-database rate
below is a vendor-published number, linked and quoted earlier in this post. The *portfolio
totals* are my extrapolation — for the metered platforms, a linear projection from real
observed usage or from the vendor's smallest always-on instance size; for self-hosting, a
rough capacity estimate assuming roughly 150–250MB of RAM per tiny idle web+DB pair, which is
my own assumption, not a vendor guarantee, and will vary with what your projects actually do.

| Approach | Pricing model | N=10 | N=50 | N=100 |
|---|---|---:|---:|---:|
| **Railway** | metered, extrapolated from my real ~$1.10/resource-mo blended rate | ~$22/mo | ~$110/mo | ~$220/mo |
| **Fly.io** (self-hosted Postgres) | metered, priced at always-on shared-cpu-1x for both app and DB machine plus a 1GB volume (a conservative ceiling — true idle-heavy traffic would bill less) | ~$40/mo | ~$202/mo | ~$403/mo |
| **Render** | fixed floor: $7 web + $6 Postgres per project | $130/mo | $650/mo | $1,300/mo |
| **Heroku** | fixed floor: $5 Eco dyno + $5 Essential-0 Postgres per project | $100/mo | $500/mo | $1,000/mo |
| **Fly.io + Managed Postgres** | metered compute, fixed-floor database: $1.94 app + $38 MPG Basic per project | $399/mo | $1,997/mo | $3,994/mo |
| **Self-hosted** (Hetzner + Coolify/Dokku/CapRover/Dokploy) | one VPS sized to fit the portfolio, cost estimated from Hetzner's verified $7.09/mo CX23 (2 vCPU/4GB) rate | ~$7/mo | ~$18–20/mo | ~$35–40/mo |

Two things jump out. First, the fixed-floor rows don't just grow — they grow by a constant
*multiple* of project count, because the floor is a per-project tax with no discount for being
quiet. Going from 10 to 100 tiny projects is a 10x increase in project count and, unsurprisingly,
almost exactly a 10x increase in the Render and Heroku bills. Second, the Fly.io + Managed
Postgres row is the cleanest proof that this is about pricing philosophy, not vendor identity:
the exact same company's own compute is nearly free at this scale, and its own managed database
product alone would run you nearly $4,000/mo for 100 tiny projects. The floor is not a Render
problem or a Heroku problem. It's what happens whenever a per-service minimum meets a large
project count, regardless of whose logo is on the invoice.

The metered and self-hosted rows, by contrast, track the actual compute involved — which for a
portfolio of small, quiet side projects is not much — and scale by roughly 10x alongside
project count too, but starting from a floor low enough that even a 10x jump stays in "forgot
to cancel a subscription" territory rather than "explain this to your spouse" territory.

## Which one should your OPC actually use?

There's no single right answer, but the decision collapses to two questions: how many
projects do you actually run, and how much does your own operational time cost you.

**If you're under about 10 tiny projects and want to spend zero time on ops,** a usage-metered
platform is the easy choice. Railway or Fly.io (self-hosting the database) will land you in
the same $15–30/mo range my own account sits in, with someone else handling TLS, backups, and
platform uptime. This is where I am today, and it's the right trade for that project count.

**If you have one or two projects that are genuinely important** — real users, revenue, or
just something you'd be upset to lose — the fixed-floor platforms earn their premium. Render's
or Heroku's managed backups, one-click restores, and support queue are worth $10–20/mo on the
project that actually matters, even while the rest of your portfolio sits on a cheaper metered
platform. Nothing says your whole portfolio has to live on one platform.

**If you're past 30–50 tiny projects,** the fixed-floor math above stops being a rounding
error and starts being real money, and that's when self-hosting starts paying for the time it
costs. A single VPS running Coolify or Dokku won't page you at 2am the way a managed
platform's status page will, and you now own that. But as the table above shows, the
multiplication is not subtle, and at OPC scale, subtlety is not what's happening to your bill.

None of this is permanent advice — the numbers above are today's, and I'll be re-running this
same math the next time my own portfolio outgrows its current platform.

## Sources and further reading

**The anchor data**
- My own Railway account, pulled live via `railway usage projects --json` and `railway list --json` on the [Railway CLI](https://docs.railway.com/reference/cli-api) — checked 2026-08-31.

**Heroku**
- Bob Wise / Heroku — [Heroku's Next Chapter](https://www.heroku.com/blog/next-chapter/) — fetched 2026-08-31
- Heroku — [pricing](https://www.heroku.com/pricing/) — fetched 2026-08-31

**Railway**
- Railway — [pricing](https://railway.com/pricing) — fetched 2026-08-31
- Railway — [public networking guide](https://docs.railway.com/guides/public-networking) — fetched 2026-08-31

**Fly.io**
- Fly.io — [pricing](https://fly.io/docs/about/pricing/) — fetched 2026-08-31
- Fly.io — [Managed Postgres](https://fly.io/docs/mpg/) — fetched 2026-08-31

**Render**
- Render — [pricing](https://render.com/pricing) — fetched 2026-08-31
- Render — [free tier limitations](https://render.com/docs/free) — fetched 2026-08-31

**Self-hosted PaaS**
- [Coolify](https://github.com/coollabsio/coolify) — fetched 2026-08-31
- [Dokploy](https://github.com/Dokploy/dokploy) — fetched 2026-08-31
- [CapRover](https://github.com/caprover/caprover) — fetched 2026-08-31
- [Dokku](https://github.com/dokku/dokku) — fetched 2026-08-31

**VPS baselines**
- Vantage — [AWS EC2 t3.medium instance pricing](https://instances.vantage.sh/aws/ec2/t3.medium) — fetched 2026-08-31
- Google Cloud — [general-purpose VM pricing](https://cloud.google.com/products/compute/pricing/general-purpose) — fetched 2026-08-31
- Hetzner — [cost-optimized cloud pricing](https://www.hetzner.com/cloud/cost-optimized/) — fetched 2026-08-31
- Hetzner — [new CX plans launch announcement, June 2024](https://www.hetzner.com/pressroom/new-cx-plans/) — fetched 2026-08-31
- Hetzner — [standardization and price adjustment announcement, May 2026](https://www.hetzner.com/pressroom/standardization-and-price-adjustment-of-our-server-products/) — fetched 2026-08-31
