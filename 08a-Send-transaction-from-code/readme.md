# How to send a transaction from your code

Transactions are how your app will interact with the chain, by reading transactions, answering to transaction events, and sending itself some transactions.

Here is a quick python sample on how to send transactions.

## Setup your env dev.

You'll need python3.6+ 

Install the requirements: in the "code" directory, you'll find a requirements.txt file.

move into that dir, and install the requirements. This will install the BismuthClient python package, that will handle all the heavy lifting for you.

`pip3 install -r requirements.txt`

You could also just install the bismuth package by `pip3 install bismuthclient`

## The code

See the sample script in "code" subdirectory.  
It should be self explanatory, but let detail:

* Import the helper object  
`from bismuthclient.bismuthclient import BismuthClient`
* Create the object, passing him the wallet file location  
`client = BismuthClient(wallet_file='wallet.der')`  
(it will create a new wallet if none is found)
* You can check what address is currently loaded:  
`print(f"My address is {client.address}")`
* Just send a transaction with the params you need!  
* Send some bis:  
`txid = client.send(recipient=client.address, amount=0)`
* Or issue a dragginator command to transfer a draggon:  
`txid = client.send(recipient="9ba0f8ca03439a8b4222b256a5f56f4f563f6d83755f525992fa5daf", operation='dragg:transfer', data='draggon_adn')`
* txid holds the transaction id if it was successful, or you get an error message, like  
`Error '['Mempool merging started from 127.0.0.1', 'Mempool: Received address: 437b30a2ea780cffb67cc220428d462cf2bedcbd3aab094aa7d4df9c', 'Mempool: Sending more than owned']'`


Full working code:
```
from bismuthclient.bismuthclient import BismuthClient

if __name__ == "__main__":
    client = BismuthClient(wallet_file='wallet.der')
    print(f"My address is {client.address}")
    txid = client.send(recipient=client.address, amount=0)  # Tries to send 0 to self
    print(f"Txid is {txid}")
```

