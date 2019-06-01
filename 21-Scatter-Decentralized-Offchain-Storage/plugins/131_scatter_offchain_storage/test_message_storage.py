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
