# Bismuth Transactions explained

Since Bismuth uses a custom bloc and transaction structure, that requires some background doc.

## Transaction structure

A BIS transaction is a list composed of the following elements

```
[
block_height,   // (int) block # of the matching transaction
timestamp,      // (str, .2f) timestamp of the transaction
from,           // (str) sender - hex format, 56 hex chars
to,             // (str) recipient - hex format, 56 hex chars
amount,         // (str, .8f) The amount of BIS to transfer
signature,      // (str) signature of the tx
pubkey,         // (str) public keykey of the sender, base64 encoded
blockhash,      // (str) hash of the block, hex format, 56 hex chars
fees,           // (str, .8f) fees for that tx
reward          // (str, .8f) coinbase reward
operation       // (str, max 30 char) - Empty for regular tx
openfield       // (str) extra data field ("Message")
]
```

### Bis transfer transaction

This is a regular BIS operation, Sarah pays John 10 BIS

```
[
block_height,   // (int) block # of the matching transaction
timestamp,      // (str, .2f) timestamp of the transaction
from,           // (str) sarah's address
to,             // (str) John's address
amount,         // (str, .8f) 10.00000000
signature,      // (str) signature of the tx by Sarah
pubkey,         // (str) public keykey of Sarah
blockhash,      // (str) hash of the block, hex format, 56 hex chars
fees,           // (str, .8f) 0.01000000
reward          // (str, .8f) 0.00000000
operation       // (str, max 30 char) - Empty for regular tx
openfield       // (str) extra data field, can be used as Message.
]
```

Sarah can use the openfield field to add a short message to the transaction.  

> This will raise the fees, and be stored forever in the chain.

Prepending the message by "msg=" will mark the transaction as a message for client apps.

A BIS message is such a transaction with a 0 BIS amount.  
You can do both BIS transfer + message in a single Transaction.

### Coinbase transaction

A coinbase transaction is the last transaction of every block.  
It's created by the miner who found a nonce with the matching difficulty and forged that block.

Coinbase transaction can be selected by "reward > 0" and may be used to get a block's timestamp.

```
[
block_height,   // (int) block # of the matching transaction
timestamp,      // (str, .2f) timestamp of the block
from,           // (str) sender - the miner's address
to,             // (str) recipient - the miner's address
amount,         // (str, .8f) 0.00000000
signature,      // (str) signature of the tx byt the miner
pubkey,         // (str) public keykey of the miner
blockhash,      // (str) hash of the block, hex format, 56 hex chars
fees,           // (str, .8f) 0.00000000 - No fees for that tx kind
reward          // (str, .8f) coinbase reward depending on the block height and elbedded tx fees
operation       // (str, max 30 char) - Empty for coinbase tx as well
openfield       // (str) matching nonce
]
```

### Abstract transaction

One of Bis strengths is to allow abstract transactions.  
These are transactions with 0 BIS involved, and data that is only understandable by the dApps who participate in that protocol.

```
[
block_height,   // (int) block # of the matching transaction
timestamp,      // (str, .2f) timestamp of the transaction
from,           // (str) sender - hex format, 56 hex chars
to,             // (str) recipient - hex format, 56 hex chars
amount,         // (str, .8f) Usually 0.00000000 but could be used as part of the protocol. Not advised though.
signature,      // (str) signature of the tx
pubkey,         // (str) public keykey of the sender, base64 encoded
blockhash,      // (str) hash of the block, hex format, 56 hex chars
fees,           // (str, .8f) fees for that tx
reward          // (str, .8f) 0.00000000
operation       // (str, max 30 char) - A selector for that abstract transaction
openfield       // (str) extra data field
]
```

The difference lies in the "operation" field, that is kind of a "command" operator.  
Convention is to use strings formated as "class:operation" to allow for easy classification.  
Say it's a kind of namespace.  
The openfield then holds the associated (short) data.

You can define your own operations, but make sure your protocol does not use already used namespaces.  
Check the existing protocols list and Contact a core dev beforehand.

See the tokens protocol for an implemented example of how this works.

### Transaction fees

BIS transaction fees are fixed and depend only on the openfield length in byte.  
Fee = 0.01 + len(openfield/100000)

### Openfield usage

> on chain storage is **not** encouraged and could be restricted in the future.  
Developpers should limit the payload to the minimum and use side chains or dApp to dApp channels to store real data.

## Transaction cycle of life

### Creation 



### Mempool insert

### Mempool sync

### Block embedding

### Onchain storage



# Interact with transactions

## How to query transactions?

## How to create transactions?
