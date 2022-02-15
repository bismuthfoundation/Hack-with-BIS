# Interacting with the Bismuth blockchain

There are many ways - and levels - you can interact with the Bismuth chain data.

We'll try to give an overview.

__WIP__

# Web or socket APIs, no need for a node

## Blockchain Explorer APIs

Bismuth explorer comes with an integrated API.  
You can use an official explorer or run your own. (Running your own is advised if you plan a high usage)

- source code: https://github.com/maccaspacca/BismuthToolsWeb (legacy explorer)  
- source code: https://github.com/maccaspacca/BismuthExplorer  
- official explorer API: https://bismuth.online/apihelp  
- explorer API: https://bismuth.im/apihelp (fallback)  

## Official API

Get live info on Bismuth servers and their state.  
WIP

https://github.com/bismuthfoundation/WalletServer/blob/master/Doc/Official_Wallet_API.md

## Wallet server API

All endpoints needed by a client wallet.  
This is what is used by official light wallets.

https://github.com/bismuthfoundation/WalletServer/blob/master/Doc/Readme.md

## WebSocket server API

WIP. To be used by html/js apps.

# With a local node

You can also rely on a local node and benefit from closer interaction with the Bismuth chain

## Native node API

With client libraries in several programmation languages and command subset reference.

https://github.com/EggPool/BismuthAPI

## Json-rpc server

An extra layer that tries to mimic bitcoind json-rpc interface and commands.  
Most of the commands needed by a wallet or exchange are implemented.  
Useful for compatibility, still the direct API is prefered for from scratch dev.

https://github.com/EggPool/BismuthRPC

## Plugins

Fastest and easiest way to get events from the chain in real time and react.  
A Bismuth exclusivity!

https://github.com/bismuthfoundation/BismuthPlugins

## Direct db access

WIP
