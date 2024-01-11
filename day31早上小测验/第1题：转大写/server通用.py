import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()

while True:
    conn,addr = sk.accept()
    while True:
        recv_msg = conn.recv(1024).decode('utf-8')
        print(recv_msg)
        send_msg = recv_msg.upper()
        conn.send(send_msg.encode('utf-8'))


    conn.close()

sk.close()