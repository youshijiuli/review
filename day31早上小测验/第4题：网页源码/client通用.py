import socket
import json
import struct


def mysend(sk, obj):
    bobj = json.dumps(obj).encode('utf-8')
    blen_bobj = struct.pack('i', len(bobj))
    sk.send(blen_bobj)
    sk.send(bobj)


def myrecv(sk):
    blen_bobj = sk.recv(4)
    len_bobj = struct.unpack('i', blen_bobj)[0]
    bobj = sk.recv(len_bobj)
    obj = json.loads(bobj.decode('utf-8'))
    return obj


sk = socket.socket()
sk.connect(('127.0.0.1',9017))

url=input('请输入网址>>>').strip()
mysend(sk,url)
text=myrecv(sk)
print(text)