# Run an ICO with BIS

This tutorial will hopefully give you all you need to launch an ICO on Bismuth.

Since basic Tokens (almost ERC20 compatible) are by default with Bismuth core, you don't need a smart contract, there will be no gas harmed, you can handle everything with your wallet and a node.

## Prerequisite

- You need a Bismuth Wallet https://github.com/hclivess/Bismuth/releases
- You probably want a fresh new bismuth address to dedicate to the ICO
- You have at least 20 BIS on that address to cover for the fees

## Create your token

From your wallet, select "misc" then "tokens", you'll get the crude tokens interface.

> **Snapshot needed**

That screen lists the existing tokens and allow for all tokens operations.  
To create a token, fill in your token name and the desired amount.  

**Important**:
- You won't be able to change the amount afterward.  
  The amount you enter here will be the total supply of your token
- Token names are all lowercase.  
  If you enter non ascii chars or uppercase, they will be converted, so use lower ascii chars only
- Keep the name short

Click "Issue", you'll be presented with a confirm popup.

> **note** Token issuance costs 10 extra $BIS in addition to the standard transaction fees.  
These fees are collected by the miners.

Once the block is mined, you have your tokens visible, and can send them as you want via the same interface.

## Auto ship your token to investors

You'll probably want an automated way of sending the tokens to the investors who will send you $BIS.

That can be done with a plugin that acts as a private smart contract.  
It checks the incoming txs to your ICO address and sends the matching tokens to the sender.

You can build on the exemple ICO plugin or use it as is, just editing the config variables.

> Plugin to be released

Of course, you can also have other interfaces, and allow your token to be bought via other cryptos or a complete different way (tweet, airdrop, lottery...)  
No limit!


## Tokens related fees

Tokens related fees are paid in $BIS, so you need a small amount of $BIS to issue or send Tokens.

- Standard Bismuth fees apply to all tokens operation: 0.01 base Fee + variable fee depending on the length of data field. 0.000011 per 10 chars
- For Token issuance, an extra 10 BIS fee is applied.
- The confirm popup show these before you can confirm.

These fees are collected by the miners.

## Resources

You can check the "token:" protocol if you want to know more about the inner working: https://github.com/bismuthfoundation/Hack-with-BIS/blob/master/01-Concepts/protocols/token.md

## Bismuth WIP

Some edges - mostly GUI - still are rough.  
We are working on the following:

- Better GUI for tokens in the wallet
- Official tokens explorer
