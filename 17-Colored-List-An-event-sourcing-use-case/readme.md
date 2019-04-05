# Colored List: An event sourcing use case

The Hypernodes rely on a "colored list" to get and update some meta paramters.  
These parameters are taken from on chain data, so every HN is supposed to have the same.

The use of Bismuth plugin allows to update these meta parameters in a safe and traceable way, with minimal overhead to the chain, as well as for the nodes.  
It's a specific use case of the "event sourcing" schema.

## The colored list

This colored list is in fact a dictionary, with "colors" string as keys, and arbitrary data as values.  
It is managed by the hypernode plugin, init at hypernode start, then kept up to date from the new blocks events.

## The event sourcing model

The dictionary is created and updated from individual specific transactions.  

- operation: `color:key_name`
- sender: POW controller address

Every tx matching both of these conditions drives an update of the corresponding key_name item of the colored list.

- updates are light: only one transaction, with little data (only one key at a time, no need to send the whole dictionary)
- operation field is only processed by hypernodes, no processing overhead for other nodes
- low update frequency anyway, these are slow changing parameters
- checks in plugin code are fast, and mean very little overhead even for hypernodes.

- In addition of the final state of the dictionary, every change from the start can be traced and audited.
- The pow controller address is hard coded, and could be a single or several distinct addresses. 'color:' operations from other addresses are just ignored.

## The code

See https://github.com/bismuthfoundation/hypernode/blob/8c76fbf1e5415b6dcdafae7820e71e0412b49544/node_plugin/__init__.py#L129
for the full_block hook that tests all new transactions and process the matching ones.
