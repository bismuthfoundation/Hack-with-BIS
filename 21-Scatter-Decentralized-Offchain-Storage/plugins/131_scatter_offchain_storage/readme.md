# S.C.A.T.T.E.R
## First usecase implementation of the Hyperlane architecture

Showcase of how a custom plugin (131_scatter_offchain_storage) can be used for decentralized offchain storage.  
To enable this plugin, simply move the "plugins" directory to your Bismuth directory and run your node.  
This plugin can be customized, for example to check if data storage has been paid for by the requestor.

> This plugin requires 035_socket_client plugin to also be in the plugins directory.

## Demo

The demo adds 2 commands SCTTR_store, SCTTR_get. There are the following demo files: 
- test_message_storage.py
-- stores  and receives messages, by default "Hi!"

- test_file_storage.py
-- stores and receives files, by default "picture.png", which you need to supply yourself

## Test client

You can test the demo plugin with a simple script like 
```
import json
import socks
import connections

s = socks.socksocket()
s.settimeout(10)
s.connect(("127.0.0.1", 5658))

connections.send(s, "SCTTR_store")  # request data storage
connections.send(s, "Hi!")  # define data to store
result = json.loads(connections.receive(s))  # receive hash of stored data
print(result)

connections.send(s, "SCTTR_get")  # request stored data
connections.send(s, result["hash"])  # share data hash
reply = connections.receive(s)  # receive data based on previous hash
print(reply)
```

## Editing and customization

For more information about custom plugins, visit https://github.com/bismuthfoundation/BismuthPlugins/tree/master/plugins/130_custom_commands

The demo SCTTR_ commands show various ways of providing params if needed:

## SCTTR_store

This command takes data to store offchain as a parameter and returns hash of the stored data.

## SCTTR_get

This command takes hash of the stored data as a parameter and returns the data from the database.

# Limitations:

This plugin is not well suited for storage of large data yet, at least not over the entire network.
