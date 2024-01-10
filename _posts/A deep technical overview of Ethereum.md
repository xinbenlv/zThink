Status: Draft

_This article is an attempt to explain the technical overview of Ethereum to a community of internet engineers. Thanks to P. Hoffman for the encouragement and discussion / review._

## State Machine

[Ethereum](https://ethereum.org) has been called "a blockchain", "a world computer", but I think the best way to think of it is to think of it as "a state machine". This state machine takes input a _state_ at the time $t$ denoted as $\sigma_{t}$  and applies a _state transition function_ $\Upsilon$ with an input _transaction_ $T$ and transition into $\sigma_{t+1}$ , written as

$$\sigma_{t+1} \equiv \Upsilon(\sigma_t, T)$$

The term "blockchain" refers to the practice that packs multiple transactions together in a data structure called a _block_, and then "chained" together via a Merkle tree.

In any point of time $t$, two different transactions $T$ and $T'$ could each be the next one accepted by the state machine, creating two possible next states. For example, when applying the $T'$, the state becomes 
$$\sigma_{t+1}' \equiv \Upsilon(\sigma_t, T')$$


Ethereum and similar blockchains are distributed systems that have multiple nodes. The term "permission-less" refers to the characteristics of certain chains, Ethereum included, to allow any nodes to join the cluster. That means these nodes aren't necessarily amicable or agree to each other.

## Execution Layer

EVM, short for "Ethereum Virtual Machine" refers to a set of rules and instruction code that forms the aforementioned state transition function.

For a transaction $T$ to be accepted, other than crypto signature validity and nonce timeliness, it mainly has to meet two state transition validation rules

1. The balance of sender in that transition needs to be greater than value being sent.
2. The data that triggers a procedure will not end with a reverting instruction opcode.*

Note: when execution ends with a reverting opcode, it also get accepts and pays gas.

Such procedure is usually referred to as "smart contract", which is a sub state machine that forms the entire world state of Ethereum state machine. See https://www.evm.codes/. 

A smart contract is a piece of code stored on the state machine and has a designated address. Commonly a smart contract is similar to an instance of a class in an object-oriented  "Deploying a smart contract" refers to the procedure that a transaction T triggers a state transition with end state $\sigma_{t+1}$ that has a new address in which the piece of code can be located and invoked in the future.

A "contract call" is mainly* invoked by sending a transaction that specifies the `to` field to be an address that exists a smart contract, and via program call convention, the first 6bytes are specifying methods of the smart contract to be called, and parameters are carried in the rest of the data field of the transaction

To explain that as an example, USDC is a digital ledger on Ethereum that company Circle use to record who currently has the balance of the USD dollars they need to payback. Beneficiaries of these "accounts" on this ledger are identified with their public keys also known as Ethereum addresses. When they sign a transaction to invoke "`transfer`" method of USDC contract, the USDC implementation of `transfer` method takes an address of recepient and value of the USDC ledger, checks the balance and determine if the request is fullfiled or rejected. 

## ERC

ERC20 is one of the standard of Ethereum that specify "tokens", or ledgers that are held in Ethereum. ERC is short for "Ethereum Request for Comment", which takes inspiration from IETF's Request for Comments. Each ERC is a standard that specify how smart contract behaves or what their interface looks like.

ERC721 is usually referred to as "Non-Fungible Token", or NFT, which specifies a ledger that records "deed". ENS, short for Ethereum Name Service, started with its own ERC which is ERC137 and grew to a family of ERCs.

## Consensus  Layer

The term "consensus mechanism" refers to the distributed algorithm, usually with game theory effect, that allows a cluster of interconnected nodes to determine which transaction to accept next and what is the current state that everyone accepts. Such mechanism usually involves introducing economics incentives for nodes to propose and/or validate transactions and blocks. Bitcoin introduces Power of Work and Longest Chain mechanism

"Longest Chain" is one of the consensus mechanism first introduced by Bitcoin. By denoting that (1) for a block to be valid, it has to has a root hash that is lower than a dynamic threshold, and (2) every nodes accept the longest chain as the ground truth, i.e. chain that currently has the longest blocks. Such arrangement, together with economics incentives of proposing blocks, creates a game theory behavior that nodes are going to form a single source of truth of which current state and chain of states there are.

"Power of Work" means that out of many nodes that are competing to propose next block, a process often referred to as "mining", the winning blocks are based on which ever blocks are having the smallest merkel tree hash but try-and-erroring different salts in the block header data structure. Such mechanism incentivise nodes to hash as many times in a short period as possible, which is energy consuming.

Ethereum started off with the same combination of consensus mechanism. Starting from Sept 2022, Ethereum changes to a new consensus mechanism called "Beacon Chain" and Proof of Stake. 

The term "Beacon Chain" means the way Ethereum determines the next block for the chain of states is to designate a block proposer to propose the next block, and a committee of nodes to validate the block and vote to accept such blocks. For such mechanism to accept any new node to become proposer and validator in a _permission-less_ manner, a Beacon Chain is created that creates beacon that coordinate timeslots in which a "term" of election will be held, and at each timeslot, and such election is held by allowing any node to commit-reveal. Being permission-less also means hostile nodes could try to manipulate timing, which is addressed in https://ethresear.ch/t/network-adjusted-timestamps/4187

The term "Proof of Stake" means to become a candidate that could be randomly elected as a member of committee or proposer, one has to stake a certain amount of native units of the ledger. In Ethereum case this is 32 ethers. 

## Other terms

The term "Oracle" refers to mechanism that introduces external input onto a blockchain. Often, oracle is a smart contract by themselves or a method plus some state variable of a smart contract.

For example, a company could provide an Oracle service to supply USD/Euro price information to a specific Ethereum contract address every hour or every day, by promising to send a new transaction that contains the USD/Euro forex rate.

ENS is another example of smart contract-based services leveraging the concept of oracle. For example, ENS sets the annual fee of each regular `.eth` name to be pegged to 5 USD but charging ethers, the native units of Ethereum ledger, called "ethers" or denoted as $ETH. When the exchange rate of ethers/USD changes, such change needs to be reflected onchain and stored in the ENS PriceOracle, periodically someone is sending the price of USD/ETH to ENS PriceOracle.  %% TODO: verify and provide more details %%

The term Layer 2 or in short "L2", in contrast to Layer 1 is widely overloaded. When used, it often refers to another blockchain featuring the capability to bundle and pack state changes onto the main chain, usually Ethereum. For example, Optimism and Arb is considered L2s of Ethereum. Layer 2 is part of the scaling attempts of blockchains and currently a few competing and maybe combining options of ZK Rollup, OP Rollup, Sharding, State Channels, the competion has not shown one winner yet.

## Reference
- Ethereum yellowpaper: https://ethereum.github.io/yellowpaper/paper.pdf
- Bitcoin whitepaper: https://bitcoin.org/bitcoin.pdf
- Timestamps: https://ethresear.ch/t/network-adjusted-timestamps/4187

