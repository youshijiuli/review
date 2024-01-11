import socket
import os

path = r'D:\My Documents\Pycharm\log'

sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9001))
while True:
    recv_msg,addr = sk.recvfrom(1024)
    print(recv_msg.decode('utf-8'))
    ip_client, port_client = addr
    # if os.path.exists(path):
    with open(path,encoding='utf-8',mode='r+') as f:
        for line in f:
            ip_file,port_file=line.strip().split('|')
            if ip_file==ip_client and port_file==port_client:
                break
        else:
            new_line=f'{ip_client}|{str(port_client)}\n'
            f.write(new_line)