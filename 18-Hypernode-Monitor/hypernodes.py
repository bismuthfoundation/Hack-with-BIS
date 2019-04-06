import sys
import json
import time
import asyncio
import hn_config
from tornado.tcpclient import TCPClient

sys.path.append(hn_config.HN_PATH)
import com_helpers
import commands_pb2
import poshelpers

S = dict()        # HN data, height, status
pingstatus = []   # HN block_height
pingversion = []  # HN version number

async def ping(i,ip,port,T):
    timeout = T
    read_timeout = T

    try:
        pingstatus[i] = 0
        tcp_client = TCPClient()
        stream = await tcp_client.connect(ip, port, timeout=timeout)
        address = hn_config.HN_ADDRESS
        hello_string = poshelpers.hello_string(port=101,address=address)
        await com_helpers.async_send_string(commands_pb2.Command.hello, hello_string, stream, ip)
        msg = await com_helpers.async_receive(stream, ip, timeout=read_timeout)

        await com_helpers.async_send_void(commands_pb2.Command.status, stream, ip)
        msg = await com_helpers.async_receive(stream, ip, timeout=read_timeout)
        if msg.command == commands_pb2.Command.status:
            data = json.loads(msg.string_value)
            pingstatus[i] = data['chain']['height']
            pingversion[i] = data['instance']['hn_version']
    except:
        pingstatus[i] = 0
        pingversion[i] = "?"

# Step 1: Contact HNs with a low timeout value
async def action(loop):
    ip = hn_config.IP
    port = hn_config.PORT
    timeout = hn_config.TIMEOUT_1
    read_timeout = hn_config.TIMEOUT_1

    tcp_client = TCPClient()
    stream = await tcp_client.connect(ip, port, timeout=timeout)
    address = hn_config.HN_ADDRESS
    hello_string = poshelpers.hello_string(port=101,address=address)
    await com_helpers.async_send_string(commands_pb2.Command.hello, hello_string, stream, ip)
    msg = await com_helpers.async_receive(stream, ip, timeout=read_timeout)

    await com_helpers.async_send_void(commands_pb2.Command.getheights, stream, ip)
    msg = await com_helpers.async_receive(stream, ip, timeout=read_timeout)
    if msg.command == commands_pb2.Command.getheights:
        S['heights'] = json.loads(msg.string_value)

    await com_helpers.async_send_void(commands_pb2.Command.status, stream, ip)
    msg = await com_helpers.async_receive(stream, ip, timeout=read_timeout)
    if msg.command == commands_pb2.Command.status:
        S['status'] = json.loads(msg.string_value)

    await com_helpers.async_send_void(commands_pb2.Command.gethypernodes, stream, ip)
    msg = await com_helpers.async_receive(stream, ip, timeout=read_timeout)
    if msg.command == commands_pb2.Command.gethypernodes:
        status = json.loads(msg.string_value)
        S['data'] = status

    L = len(status)

    task = []
    for i in range(0,L):
        data = status[i]
        pingstatus.append(0)
        pingversion.append("?")
        task.append(loop.create_task(ping(i,data[1],data[2],timeout)))

    for i in range(0,L):
        await task[i]

    return status

# Step 2: Re-try with higher timeout HNs which timed out in Step 1 (pingstatus == 0)
async def action2(loop,status):
    timeout = hn_config.TIMEOUT_2
    L = len(status)

    task = []
    N = 0
    for i in range(0,L):
        data = status[i]
        if pingstatus[i] == 0:
            task.append(loop.create_task(ping(i,data[1],data[2],timeout)))
            N = N + 1

    for i in range(0,N):
        await task[i]

# Count number of HNs which timed out
def count_zeros(T):
    L = len(pingstatus)
    y = 0
    for i in range(0,L):
        if pingstatus[i]==0:
            y = y + 1

    print("Number of {} sec Timeouts = {}".format(T,y))


def status_height(status):
    S = dict()
    L = len(pingstatus)
    for i in range(0,L):
        ip = status[i][1]
        if pingstatus[i] == 0:
            S[ip] = -1
        else:
            S[ip] = pingstatus[i]
    return S

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    status = event_loop.run_until_complete(action(event_loop))
    count_zeros(hn_config.TIMEOUT_1)

    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(action2(event_loop,status))
    count_zeros(hn_config.TIMEOUT_2)

    nodes = status_height(status)

    L = len(pingstatus)
    for i in range(0,L):
        ip = status[i][1]
        port = status[i][2]
        ip_port = ip + ":0" + port
        H2 = pingstatus[i]
        ver = pingversion[i]
        try:
            S['heights'][ip_port]['height']=H2
            S['heights'][ip_port]['version']=ver
        except:
            S['heights'][ip_port]={'height':H2, 'version':ver}

        i = i + 1

with open(hn_config.OUTFILE_1, 'w') as outfile:
    json.dump(nodes, outfile)

with open(hn_config.OUTFILE_2, 'w') as outfile:
    json.dump(S, outfile)
