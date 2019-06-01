import json
import socks
import connections
import base64

def decompress(data, file):
    print(data)
    with open(file, "wb") as outfile:
        outfile.write(base64.b85decode(data))

def compress(file):
    with open(file, 'rb') as infile:
        contents = base64.b85encode(infile.read()).decode()
        print(contents)

    return contents

s = socks.socksocket()
s.settimeout(10)
s.connect(("127.0.0.1", 5658))

connections.send (s, "SCTTR_store") #request data storage
connections.send (s, compress("picture.png")) #define data to store
result = json.loads(connections.receive (s)) #receive hash of stored data
print ("result",result)

connections.send (s, "SCTTR_get") #request stored data
connections.send (s, result["hash"]) #share data hash
reply = connections.receive (s) #receive data based on previous hash
print("reply",reply)
decompress(reply, "test.png")