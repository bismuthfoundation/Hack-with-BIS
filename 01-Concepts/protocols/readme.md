# Bismuth Abstract protocols

Bismuth allow any dev to define its own protocols and actions on top of the BIS blockchain.

This is a list of currently known protocol and operations.

> If you plan to add a custom operation class for your use, please check this list beforehand and contact a core dev.  
  Of course, you can also built upon existing protocols (like tokens, events) if they suit your needs.

By convention, we refer to the protocol by their "class:" operation handle.

# Core Bismuth Protocols

These protocols are hard coded in Bismuth core or in the Hypernodes.

## Alias

The "alias:" protocol allows for registration of on-chain alias of your address

TODO

## Token

The "token:" protocol allows for BIS tokens management: issuance and transfer.

TODO

## Hypernode

Handles registration and unregistration of the hypernodes.

https://github.com/bismuthfoundation/hypernode/blob/master/doc/registration_rules.md

# Bismuth team protocols

## Twitter

The "twitter:" protocol is used by the twitter giveaway bot.

TODO

## Event

The "event:" protocol is used by the event sourcing demo dApp.

https://github.com/EggPool/BismuthEvents/blob/master/doc/events.md


# Third party protocols

## Dragg

The "dragg:" protocol is used by the https://dragginator.com dApp.

