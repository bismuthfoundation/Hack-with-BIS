# Bismuth Execution model

The current Bismuth model is very different from the Ethereum one.
You simply can't transpose what is done with smart contracts and solidity.
Bismuth does not need public "smart" contracts atm, and does not have a VM where every nodes executes the same code.

Although it could be seen as a limitation, it's in fact quite a strength, and some exploits that have taken place with ETH smart contracts could not have been successful on a Bismuth like architecture.

## "Smart" contracts vs "smart" protocols in a nutshell

ETH like smart contract are written in a specific language, stored on chain, and run **IN** every node.

Bismuth like smart protocols are implemented **ON TOP** of the Bismuth chain and only run by concerned dApps.

## Ethereum

- You have to learn a new language, Solidity
- There are some specific pitfalls (underflow, visibility, access rights)
- Flawed contract code can give an infinity of coins to a user
- Several hacks and horror stories already in Eth smart contracts History
- Smart contracts can "own" funds 
- smart contracts live in the chain forever and can't be stopped nor upgraded unless the author provided a kill switch
- if there is a kill switch, the owner can get all the funds of a contract.
- every contract invocation is processed by every single eth node in a VM - Virtual Machine - and consumes gas
- contracts can not directly access outside resources

Eth model has some strengths and some use cases that you could simply not replicate with BIS, but BIS has other uses.

## Bismuth

- No new language to learn. You can write contracts and protocols in almost any language, Python being the native language.
- No more pitfalls than with your usual code
- Contracts can't overspend
- No VM, no "on chain" code, no public contracts
- Users can run private contracts
- Owners then have full control (fix, upgrade) over the contract.
- The contract, if its inner working is published, is fully auditable and verifiable
- Contract invocation are only run by the clients that have an interest in that specific contract
- Private contracts can do anything, including accessing outside data without the need for on chain oracles


## Bismuth tokens

Things that are to be widely used, like tokens, are not handled via a generic VM and user code.  
If a use case is wanted enough, it can be integrated in Bismuth core.  
The Bismuth dev team does not have the weight of Bitcoin or ETH, and can move forward very very fast.

That's the case with tokens.
- native tokens
- optimized, resource savy tokens, indexed db of tokens
- still can be overloaded with extra features
- code is tested, public, the same for everyone: potential bugs are identified and can be fixed globaly

To match ETH terminology, current Bismuth tokens are partially ERC20 compliant.  
They do not allow delegation (no approve/allowance): you can't have someone else spend your tokens and approve.

More feature packed tokens types may be added soon.

## Bismuth "Smart" protocols

Rather than having immutable on chain code, that has all power on the funds and can have them destroyed or locked up, plus is run by every single node, Bismuth favors the concept of "smart" protocols.  

> I use the quotes, because no contract/protocol in crypto is really "smart". It's just code that is as smart - or dumb - as the dev who wrote it.

A protocol is based upon the Bismuth transactions, that can be considered as abstract data.  
It's an agreement between 2 or more parties on what that data means, and what to do when an event occurs.  

- Only clients that are involved in a protocol need to read the data and run the code. Not every node.
- Code is not on chain. Can be updated, fixed, does not clobber the chain, does not consume node resources.
- They are a "contract" between agreeing parties, with the logic ideally being public
- Anyone can run the logic over the on chain data and verify that everyone acted as they should.
- Protocols can evolve, be overloaded, or serve as basis for more evolved protocols.
- Protocols can use protocols... for instance, a protocol could define valid implementations (with on chain hash) of itself.

See the existing Bismuth protocols: https://github.com/bismuthfoundation/Hack-with-BIS/tree/master/01-Concepts/protocols

# References

Some Eth Horror stories, showing whatever the architecture, buggy code can be a mess.  
Immutable buggy code, even more.

- How to Not Destroy Millions in Smart Contracts (Pt. 1)  
  https://hackernoon.com/how-to-not-destroy-millions-in-smart-contracts-pt-1-bdefac3656b7
- How to Not Destroy Millions in Smart Contracts (Pt. 2)  
  https://hackernoon.com/how-to-not-destroy-millions-in-smart-contracts-pt-2-85c4d8edd0cf
- Regarding Eth: "Eth: So far, this particular choice of design has resulted in more than half a billion dollar being compromised in one way or the other"  
  https://hackernoon.com/yes-this-kid-really-just-deleted-150-million-dollar-by-messing-around-with-ethereums-smart-2d6bb6750bb9

# FAQ

## If the code is not on chain, you have to trust the owner of the contract?
Yes. Kinda. Like you trust an Eth smart contract owner not to kill it and get all the funds, or like you trust him to have written bugless code that will run 10's of years without any possible tweak.  

As a matter of fact, ETH and solidity could be more suited for purely currency automated transfers, whereas BIS protocols allows for easier to dev, run and maintain complex apps on top of the blockchain.

## if there are several implementations of a protocol, what if one implementation does not works as intended, or tries to cheat?
Would you trust an unknown software provider with a bitcoin wallet?  
You don't.  
Once you give your keys to an app, that app virtually can do anything with the funds/data.  
Why open source and reputation are so important.  

In the event of a cheating app, however, this would just impact the specific users of this app.  
Since this app would emit data or transactions that does not comply to the protocol, those transactinos will be ignored by the legit apps.  
You can see that as a "virtual" fork in the protocol state.
