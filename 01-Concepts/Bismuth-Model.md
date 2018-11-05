# Bismuth Execution model

The current Bismuth model is very different from the Ethereum one.
You simply can't transpose what is done with smart contracts and solidity.
Bismuth does not need public "smart" contracts atm, and does not have a VM where every nodes executes the same code.

Although it could be seen as a limitation, it's in fact quite a strength, and many exploits that have taken place with ETH smart contracts simply could not have been done on a Bismuth like architecture.


## Ethereum

- You have to learn a new language, Solidity
- There are severe pitfalls (underflow, visibility, access rights)
- Flawed contracts can give an infinity of coins to a user
- Several hacks and horror stories already in Eth smart contracts History
- Smart contracts can "own" funds 
- smart contracts live in the chain forever and can't be stopped nor upgraded unless the author provided a kill switch
- bugs or flaws are forever
- if there is a kill switch, the owner will get all the funds.
- every contract invocation is processed by every single eth node in a VM - Virtual Machine - and consumes gas
- contracts can not directly access outside resources

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

Moreover:

## Bismuth tokens

Things that are to be widely used, like tokens, are not handled via a generic VM and some buggy user code.  
If a use case is wanted enough, it can be integrated in Bismuth core.  
The Bismuth dev team does not have the weight of Bitcoin or ETH, and can move forward very very fast.

That's the case with tokens.
- native tokens
- optimized, resource savy tokens, indexed db of tokens
- still can be overloaded with extra features
- code is tested, public, the same for everyone: potential bugs are identified and can be fixed globaly

To match ETH terminology, current Bismuth tokens are partially ERC20 compliant.  
They do not allow delegation (no approve/allowance): you can't have someone else spend your tokens and approve.

## Bismuth Smart protocols

Rather than having immutable on chain code, that has all power on the funds and can have them destroyed or locked up, and is run by every single node, Bismuth favors the concept of "smart" protocols.

A protocol is based upon the Bismuth transactions, that can be considered as abstract data.  
It's an agreement between 2 or more parties on what that data means, and what to do when an event occurs.  

- Only 

# References


