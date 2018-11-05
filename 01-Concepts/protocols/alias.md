# Alias

Bismuth core Alias functionality

> Note: Aliases currently use openfield only.  
A move to alias: operation is possible in the future.

## Purpose

Allow a user to register an Alias (string) for his Bismuth address.  
That alias may then be used by the wallets or apps as label.

> Important: An alias registration adds 1 BIS to the transaction fees.

## Maintainer

Bismuth core team.

## Operations list

### Current working

- No operation, transaction to self where openfield starts with "alias="
- Client first checks that the alias to register does not already exists.

# Evolution proposal

> This is *NOT* active yet

### Proposal: alias:register

- Operation: "alias:register"  
- Openfield contains the alias string to associate to the sender's address.
- Should verify - on node - that the alias does not already exists.

### Proposal: alias:transfer

- Operation: "alias:transfer"  
- Openfield contains "recipient:alias"
- Allows to transfer an alias to another address. checks that sender is the owner of the alias

### Proposal: alias:free

- Operation: "alias:free"  
- Openfield contains the alias string
- Frees an alias so it can be used by anyone.

## Usage

Query the db for the last alias associated to a given address, or for the list of all historical aliases.  
Display alias instead or in addition to the address.

> Since it's part of Bismuth core, Aliases are extracted from the chain as the event occur (on mined transaction reception) and are indexed into a specific table for performance reasons.

## Related resources

- Part of Bismuth Core: https://github.com/hclivess/Bismuth/

## Licence

Bismuth core is GPL
