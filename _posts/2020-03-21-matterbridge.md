---
title: "3min connect Slack and Discord with matterbridge"
date: 2020-03-21T14:41:00-08:00
categories:
  - blog
tags:
  - Jekyll
  - update
---

In our case, we want to have a bridge to connect channels between Slack and Discord.

I found [matterbridge](https://github.com/42wim/matterbridge). Within 3min I was able to run a bridge on my mac.

## Pre-requisite

### Get Token
First off, certainly you will need to have a Discord server and Slack workspace, and you will need admin power in both for creating the token.

To obtain the token for Slack, here we refer to a legacy-token, it's legacy and thus not recommended. Follow [Slack official instruction](https://slack.com/help/articles/215770388-Create-and-regenerate-API-tokens), you could go to `api.slack.com/custom-integrations/legacy-tokens.` and follow instruction to obtain a token.

To obtain th token for Discord, you will need create a Discord Bot, and then obtain its token. Follow [this instruction](https://www.writebots.com/discord-bot-token/) to get a discord bot and its token.

### Install Docker
Secondly you will need to have [Docker](https://docs.docker.com/) if you haven't install it.

## Step 1: the config
The configuration for matterbridge is written in `toml`, and there is a [slack to discord example] but I slightly tweak the example to make it easier to understand, **everything with a`<>` here needs to be changed.**, others don't.

```
[slack]
[slack.test]
Token="<yourslacktoken>"
PrefixMessagesWithNick=true

[discord]
[discord.test]
Token="<yourdiscordtoken>"
Server="<your-discord-server-name>"

[general]
RemoteNickFormat="[{PROTOCOL}/{BRIDGE}] <{NICK}> "

[[gateway]]
    name = "mygateway"
    enable=true

    [[gateway.inout]]
    account = "discord.test"
    channel="general"

    [[gateway.inout]]
    account ="slack.test"
    channel = "general"
```
## Step 2: Run the dockerised version
See: [Instructon running matterbridge on Docker](https://github.com/42wim/matterbridge/wiki/Deploy:-Docker)

```
docker run -ti -v <path-to-toml-config>:/matterbridge.toml 42wim/matterbridge
```

![2020-03-21 matterbridge final cmd](http://blog.zzn.im/wp-content/uploads/2020/03/2020-03-21_14-09-45-300x61.png)

And now you shall be able to send message from one and see it in another.