import socket
import json
import struct
import requests

def mysend(conn,obj):
    bobj = json.dumps(obj).encode('utf-8')
    blen_bobj = struct.pack('i',len(bobj))
    conn.send(blen_bobj)
    conn.send(bobj)

def myrecv(conn):
    blen_bobj=conn.recv(4)
    len_bobj=struct.unpack('i',blen_bobj)[0]
    bobj=conn.recv(len_bobj)
    obj=json.loads(bobj.decode('utf-8'))
    return obj

sk = socket.socket()
sk.bind(('127.0.0.1',9017))
sk.listen()
conn,_ =sk.accept()

url=myrecv(conn)
try:
    ret=requests.get(url)
    msg=ret.content.decode('utf-8')
except Exception:
    msg='您输入的网页不存在！'
mysend(conn,msg)