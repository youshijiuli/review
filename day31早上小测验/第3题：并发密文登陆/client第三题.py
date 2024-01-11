import socket
import struct
import hashlib
import os

def encrypt(username,password):
    md5=hashlib.md5(username.encode('utf-8'))
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

sk = socket.socket()
sk.connect(('127.0.0.1',9001))
status=b'N'

while status==b'N':
    username=input('请输入用户名>>>').strip()
    password=input('请输入密码>>>').strip()
    cipertext=encrypt(username,password)
    send_msg=(username+'|'+cipertext).encode('utf-8')
    blen_send_msg=struct.pack('i',len(send_msg))
    sk.send(blen_send_msg)
    sk.send(send_msg)

    status=sk.recv(1)
    if status==b'Y':
        print('登陆成功!')
    else:
        print('用户名或密码错误，请重新登陆！')
