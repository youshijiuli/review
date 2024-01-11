import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
server = ('127.0.0.1',9001)
while True:
    send_msg = input('>>>')
    if send_msg.upper() == 'Q': break
    sk.sendto(send_msg.encode('utf-8'),server)