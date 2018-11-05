# Bismuth Abstract protocols

Bismuth allow any dev to define its own protocols and actions on top of the BIS blockchain.

This is a list of currently known protocol and operations.

> If you plan to add a custom operation class for your use, please check this list beforehand and contact a core dev.  
  Of course, you can also built upon existing protocols (like tokens, events) if they suit your needs.

By convention, we refer to the protocol by their "class:" operation handle.  
Also see https://github.com/bismuthfoundation/Hack-with-BIS/blob/master/01-Concepts/Transaction.md#abstract-transaction

# Core Bismuth Protocols

These protocols are hard coded in Bismuth core or in the Hypernodes.

## Alias

The "alias:" protocol allows for registration of on-chain alias of your address

https://github.com/bismuthfoundation/Hack-with-BIS/blob/master/01-Concepts/protocols/alias.md

## Color

The "color:" protocol is used as part of the hypernodes to manage colored lists and sync them across the network.

TODO

## Hypernode

Handles registration and unregistration of the hypernodes.

https://github.com/bismuthfoundation/hypernode/blob/master/doc/registration_rules.md


## Protocol

The "protocol:" protocol is reserved for future use.


## Token

The "token:" protocol allows for BIS tokens management: issuance and transfer.

https://github.com/bismuthfoundation/Hack-with-BIS/blob/master/01-Concepts/protocols/token.md


# Bismuth team protocols

## Event

The "event:" protocol is used by the event sourcing demo dApp.

https://github.com/EggPool/BismuthEvents/blob/master/doc/events.md

> Note: this was drafted before the "operation" field and only uses openfield, will be converted later on.  
The protocol class still is reserved.


## Twitter

The "twitter:" protocol is used by the twitter giveaway bot.

TODO

# Third party protocols

## Dragg

The "dragg:" protocol is used by the https://dragginator.com dApp.

