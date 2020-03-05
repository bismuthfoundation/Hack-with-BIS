"""
Demo of the 131_scatter_offchain_storage plugin.  
Place this file in the Bismuth node directory.
"""

import json
import socks
from base64 import b85encode, b85decode

import connections

def decode(input, file):
    data = json.loads(input)
    with open(file, "wb") as outfile:
        outfile.write(b85decode(data['data']))

def encode(file):
    """Encodes binary file into base85 ascii so it can be sent over json 
    (required by low level bismuth transport layer)"""
    with open(file, "rb") as infile:
        contents = b85encode(infile.read()).decode()
        print(contents)

    return contents

s = socks.socksocket()
s.settimeout(10)
s.connect(("127.0.0.1", 5658))

connections.send(s, "SCTTR_store")  # request data storage
connections.send(s, encode("picture.png"))  # define data to store
result = json.loads(connections.receive(s))  # receive hash of stored data
print("result", result)

connections.send(s, "SCTTR_get")  # request stored data
connections.send(s, result["hash"])  # share data hash
reply = connections.receive(s)  # receive data based on previous hash
print("reply", reply)
decode(reply, "test.png")
