import struct
import os
import socketserver

path=r'C:\Users\oddgod\Desktop\第3题：并发密文登陆\data'

class Myserver(socketserver.BaseRequestHandler):

    def handle(self):

        conn = self.request

        while True:
            status=b'N'

            while status==b'N':

                blen_recv_msg = conn.recv(4)
                len_recv_msg = int(struct.unpack('i', blen_recv_msg)[0])
                recv_msg = conn.recv(len_recv_msg).decode('utf-8')
                input_username,input_cipertext=recv_msg.split('|',1)

                with open(path,encoding='utf-8') as f1:
                    for line in f1:
                        username, cipertext = line.strip().split('|')
                        if input_username == username and input_cipertext == cipertext:
                            status=b'Y'

                            break
                    else:
                        status=b'N'

                conn.send(status)

server = socketserver.ThreadingTCPServer(('127.0.0.1',9001),Myserver)
server.serve_forever()