# Bismuth concepts

A quick overview of main Bismuth concepts.

## No public smart contract

The current Bismuth model is very different from the Ethereum one.  
You simply can't transpose what is done with smart contracts and solidity.  
Bismuth does not need public "smart" contracts atm, and does not have a VM where every nodes executes the same code.

See Bismuth Execution model: https://github.com/bismuthfoundation/Hack-with-BIS/blob/master/01-Concepts/Bismuth-Model.md


## The Bismuth Transactions

BIS comes with 3 different types of transactions, unified under a common structure.  
https://github.com/bismuthfoundation/Hack-with-BIS/blob/master/01-Concepts/Transaction.md

## Interacting with Bismuth

There are many ways to interact with the Bismuth blockchain, depending on the kind of data you need, and wether you have a local node running or not.  
Here is an overview:  
https://github.com/bismuthfoundation/Hack-with-BIS/blob/master/01-Concepts/Interacting.md

## Current Bismuth Protocols

"Smart" abstract protocols are an essential part of Bismuth.  
Transactions can make use of the "operation" field to emulate abstract behaviour, that only protocol aware apps can then interpret.  
The nodes then process these transactions as abstract data, not needing any processing by unrelated clients.

https://github.com/bismuthfoundation/Hack-with-BIS/tree/master/01-Concepts/protocols


# WIP


## Abstract data

## Off chain data and checkpointing

## For your eyes only

## State channels

## Private contracts
