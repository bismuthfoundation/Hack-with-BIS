#Bismuth State Channels

The concept of Bismuth state channels comes from an idea that it is possible 
to keep an objective consensus around behavior and results of on-chain contracts, without 
the need of the contract to be hosted on the Bismuth network itself.

The state channel network is built around source data hashes of contracts content
and around hashes of behavior of those contracts or references to them, although we only 
need to keep consensus around contract behavior, exploiting Vitalik Buterin's data 
unavailability phenomenon for contract content hashes. State channels don't have to be 
limited to contracts. 

In fact,
they can act as anchors for opinion on any information, as long as more than 50% of
 participants remain truthful - such situation needs to be enforced by incentives for the
 historic performance in consensus. 

```
hash(Contract) → ContractHash
hash(ContractBehavior) → ContractBehaviorHash
```
 example:
 
```
import base64
from hashlib import blake2b

contract_list = {}
example_consensus = {"node1":None, "node2":None, "node3":"evil"}

def hashfunction(data):
    blake2bhash = blake2b(data.encode(), digest_size=20).hexdigest()
    return blake2bhash

contract1_raw = base64.a85encode("imasuperlongcontract".encode("utf-8"))

contract1 = base64.a85decode(contract1_raw)
contract1_hash = hashfunction(contract1.decode("utf-8"))
print (contract1_hash)

contract1_behavior = base64.a85encode("allrelatedblockchaincommunication".encode("utf-8"))
contract1_behavior_hash = hashfunction(contract1_behavior.decode("utf-8"))

contract_list[contract1_hash]=contract1_behavior_hash
print(contract_list)

example_consensus ["node1"] = contract_list
example_consensus ["node2"] = contract_list
print (example_consensus)
```
 
 References:
 * https://github.com/ethereum/research/wiki/A-note-on-data-availability-and-erasure-coding