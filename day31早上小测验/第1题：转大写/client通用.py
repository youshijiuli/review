import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9001))

while True:
    send_msg = input('>>>')
    sk.send(send_msg.encode('utf-8'))
    if send_msg.upper() == 'Q': break
    recv_msg = sk.recv(1024).decode('utf-8')
    if recv_msg.upper() == 'Q': break
    print(recv_msg)


sk.close()