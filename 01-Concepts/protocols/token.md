# Token


## Purpose

Handle Bismuth Tokens issuance, charges, and transfer.

> Important: A token issuance adds 10 BIS to the transaction fees.

## Maintainer

Bismuth core team.

## Operations list

### token:issue

- Operation: `token:issue`
- Openfield contains `TokenName:TokensQuantity`
- TokenName will be converted to all lower case, it's the name of the token
- TokensQuantity is an integer
- Issuance will fail if the token already was issued  
  (but fees still will be processed and the transaction still will be recorded in the chain)
- Credit "TokensQuantity" tokens of name "tokenname" to the sender.

### token:transfer

- Operation: `token:transfer`
- Openfield contains `TokenName:TokensQuantity`
- TokenName will be converted to all lower case, it's the name of the token to be transfered
- TokensQuantity is an integer
- Transfer will fail if sender does not have enough tokens of that name  
  (but the transaction still will be recorded in the chain)
- Debit "TokensQuantity" tokens of name "tokenname" from the sender and credit them to the recipient of the transaction.

**Update, keeping compatibility with core node implementation**

> To account for protocol extension, optional data can be given in Openfield after `TokenName:TokensQuantity`, like  
> `TokenName:TokensQuantity:Anything_really`
> Such data will be ignored by the core protocol.  
> The recommended format for that optional data is a json dictionary, so to provide a typed and unambiguous payload.

For instance, a common subprotocol could be to add a message to a token transfer, using as Openfield   
`TokenName:TokensQuantity:{"Message":"My custom message"}`  

Another compatible subprotocol could add a txid as reference to a token transfer, using as Openfield  
`TokenName:TokensQuantity:{"TxId":"some_previous_bismuth_tx_id"}`  

## Usage

Tokens are processed and indexed in a dedicated table within the core node code.  
Users should use the native API commands or direct DB query in the tokens table to get tokens info, rather than re-implementing the protocol themselves.

> Note: Some tokens were created with tokens v1 (no opration yet) and thus would not be valid if the whole chain was to be reindexed.  
A Whole protocol re-implementation would need to handle both tokens v1 or v2 depending on the creation date.

The tokens operations are - crudly - supported by the GUI wallet.

## Related resources

- Part of Bismuth Core: https://github.com/hclivess/Bismuth/
- https://github.com/hclivess/Bismuth/blob/master/tokensv2.py

## Licence

Bismuth core is GPL
