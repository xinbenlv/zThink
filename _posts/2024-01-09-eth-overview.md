---
title: A deep technical overview of Ethereum
date: 2024-01-09T22:14:51-08:00
categories:
  - blog
tags:
  - Jekyll
  - update
  - Ethereum
status: draft
---
_This article is an attempt to explain the technical overview of Ethereum to a community of internet engineers. Thanks to P. Hoffman for the encouragement and discussion/review._

Status
## State Machine

[Ethereum](https://ethereum.org) has been called "a blockchain," "a world computer," but I think the best way to think of it is as "a state machine." This state machine takes input, a _state_ at time $t$ denoted as $\sigma_{t}$, and applies a _state transition function_ $\Upsilon$ with an input _transaction_ $T$ and transitions into $\sigma_{t+1}$, written as

$$\sigma_{t+1} \equiv \Upsilon(\sigma_t, T)$$

The term "blockchain" refers to the practice of packing multiple transactions together in a data structure called a _block_ and then "chaining" them together via a Merkle tree.

At any point in time $t$, two different transactions $T$ and $T'$ could each be the next one accepted by the state machine, creating two possible next states. For example, when applying $T'$, the state becomes 
$$\sigma_{t+1}' \equiv \Upsilon(\sigma_t, T')$$

Ethereum and similar blockchains are distributed systems with multiple nodes. The term "permission-less" refers to the characteristics of certain chains, including Ethereum, that allow any nodes to join the cluster. That means these nodes aren't necessarily amicable or in agreement with each other.

## Execution Layer

EVM, short for "Ethereum Virtual Machine," refers to a set of rules and instruction code that forms the aforementioned state transition function.

For a transaction $T$ to be accepted, other than crypto signature validity and nonce timeliness, it mainly has to meet two state transition validation rules:

1. The balance of the sender in that transition needs to be greater than the value being sent.
2. The data that triggers a procedure will not end with a reverting instruction opcode.*

Note: when execution ends with a reverting opcode, it also gets accepted and pays gas.

Such a procedure is usually referred to as a "smart contract," which is a sub-state machine that forms the entire world state of the Ethereum state machine. See https://www.evm.codes/. 

A smart contract is a piece of code stored on the state machine and has a designated address. Commonly, a smart contract is similar to an instance of a class in an object-oriented language. "Deploying a smart contract" refers to the procedure in which a transaction T triggers a state transition with an end state $\sigma_{t+1}$ that has a new address in which the piece of code can be located and invoked in the future.

A "contract call" is mainly* invoked by sending a transaction that specifies the `to` field to be an address that corresponds to a smart contract. Via program call convention, the first 6 bytes specify the methods of the smart contract to be called, and parameters are carried in the rest of the data field of the transaction.

To explain this with an example, USDC is a digital ledger on Ethereum that the company Circle uses to record who currently holds the balance of the USD dollars they need to pay back. Beneficiaries of these "accounts" on this ledger are identified with their public keys, also known as Ethereum addresses. When they sign a transaction to invoke the "`transfer`" method of the USDC contract, the USDC implementation of the `transfer` method takes an address of the recipient and the value of the USDC ledger, checks the balance, and determines if the request is fulfilled or rejected.

## ERC

ERC20 is one of the standards of Ethereum that specifies "tokens," or ledgers that are held in Ethereum. ERC is short for "Ethereum Request for Comment," which takes inspiration from IETF's Request for Comments. Each ERC is a standard that specifies how a smart contract behaves or what its interface looks like.

ERC721 is usually referred to as a "Non-Fungible Token," or NFT, which specifies a ledger that records "deeds." ENS, short for Ethereum Name Service, started with its own ERC, which is ERC137, and grew to a family of ERCs.

## Consensus Layer

The term "consensus mechanism" refers to the distributed algorithm, usually with a game theory effect, that allows a cluster of interconnected nodes to determine which transaction to accept next and what is the current state that everyone accepts. Such a mechanism usually involves introducing economic incentives for nodes to propose and/or validate transactions and blocks. Bitcoin introduces the Proof of Work and Longest Chain mechanism.

"Longest Chain" is one of the consensus mechanisms first introduced by Bitcoin. It denotes that (1) for a block to be valid, it has to have a root hash that is lower than a dynamic threshold, and (2) every node accepts the longest chain as the ground truth, i.e., the chain that currently has the longest blocks. Such an arrangement, together with the economic incentives of proposing blocks, creates a game theory behavior where nodes form a single source of truth for the current state and chain of states.

"Proof of Work" means that out of many nodes competing to propose the next block, a process often referred to as "mining," the winning blocks are based on whichever blocks have the smallest Merkle tree hash but try-and-error different salts in the block header data structure. Such a mechanism incentivizes nodes to hash as many times as possible in a short period, which is energy-consuming.

Ethereum started off with the same combination of consensus mechanisms. Starting from September 2022, Ethereum changed to a new consensus mechanism called "Beacon Chain" and Proof of Stake.

The term "Beacon Chain" means that Ethereum determines the next block for the chain of states by designating a block proposer to propose the next block and a committee of nodes to validate the block and vote to accept such blocks. For such a mechanism to accept any new node to become a proposer and validator in a _permission-less_ manner, a Beacon Chain is created that coordinates timeslots in which a "term" of election will be held. At each timeslot, such an election is held by allowing any node to commit-reveal. Being permission-less also means hostile nodes could try to manipulate timing, which is addressed in https://ethresear.ch/t/network-adjusted-timestamps/4187.

The term "Proof of Stake" means that to become a candidate that could be randomly elected as a member of the committee or proposer, one has to stake a certain amount of native units of the ledger. In Ethereum's case, this is 32 ethers.

## Other Terms

The term "Oracle" refers to a mechanism that introduces external input onto a blockchain. Often, an oracle is a smart contract by itself or a method plus some state variable of a smart contract.

For example, a company could provide an Oracle service to supply USD/Euro price information to a specific Ethereum contract address every hour or every day, by promising to send a new transaction that contains the USD/Euro forex rate.

ENS is another example of a smart contract-based service leveraging the concept of an oracle. For example, ENS sets the annual fee of each regular `.eth` name to be pegged to 5 USD but charges ethers, the native units of the Ethereum ledger, called "ethers" or denoted as $ETH. When the exchange rate of ethers/USD changes, such a change needs to be reflected on-chain and stored in the ENS Price Oracle. Periodically, someone sends the price of USD/ETH to the ENS Price Oracle. %% TODO: verify and provide more details %%

The term Layer 2 or in short "L2," in contrast to Layer 1, is widely overloaded. When used, it often refers to another blockchain featuring the capability to bundle and pack state changes onto the main chain, usually Ethereum. For example, Optimism and Arb are considered L2s of Ethereum. Layer 2 is part of the scaling attempts of blockchains, and currently, a few competing and maybe combining options of ZK Rollup, OP Rollup, Sharding, State Channels, the competition has not shown one winner yet.

## Reference
- Ethereum yellowpaper: https://ethereum.github.io/yellowpaper/paper.pdf
- Bitcoin whitepaper: https://bitcoin.org/bitcoin.pdf
- Timestamps: https://ethresear.ch/t/network-adjusted-timestamps/4187
