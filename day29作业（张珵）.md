# day29作业（张珵）

# 1.基于tcp协议完成登录认证

```
    客户端输入用户名密码
    发送到服务端
    服务端认证
    发送结果到客户端
```

**server**

```python
import socket

path=r'D:\data'

sk = socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()
conn,addr = sk.accept()

recv_msg = conn.recv(1024)
username,password=recv_msg.decode('utf-8').split('|')
with open(path,encoding='utf-8') as f:
    for line in f:
        nm, pwd = line.strip().split('|')
        if username == nm and password == pwd:
            send_msg = '登陆成功！'
            break
    else:
        send_msg='用户名或密码错误，登陆失败！'
conn.send(send_msg.encode('utf-8'))
conn.close()

sk.close()
```

**client**

```python
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9001))

username=input('请输入用户名>>>').strip()
password=input('请输入密码>>>').strip()

sk.send((username+'|'+password).encode('utf-8'))
recv_msg = sk.recv(1024)
print(recv_msg.decode('utf-8'))

sk.close()
```



# 2.基于udp协议的多人聊天

```
    自动识别用户 不能用ip和port
```
**server**

```python
import socket
import random
sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9001))
dic={}      #使用字典保存每个name对应的字体颜色font_color和背景颜色back_color
while True:
    recv_msg,addr = sk.recvfrom(1024)
    recv_msg=recv_msg.decode('utf-8')
    name=recv_msg.split(':',1)[0]
    if name in dic:
        font_color = dic[name][0]
        back_color = dic[name][1]
    else:
        font_color = random.randint(30, 37)     #随机生成一个字体颜色
        while True:
            back_color = random.randint(40, 47) #随机生成一个背景颜色
            if back_color != font_color + 10:   #确保背景颜色与字体颜色不同
                break
        dic[name]=(font_color,back_color)
    print('\033[1;'+str(font_color)+';'+str(back_color)+'m'+recv_msg+'\033[0m')
    send_msg = input('>>>')
    sk.sendto(send_msg.encode('utf-8'),addr)
```

**client**

```python
import socket

name=input('请输入您的名字>>>').strip()
sk = socket.socket(type=socket.SOCK_DGRAM)
server = ('127.0.0.1',9001)
while True:
    send_msg = input('请输入您的留言>>>')
    if send_msg.upper() == 'Q': break
    send_msg = name+': '+send_msg
    sk.sendto(send_msg.encode('utf-8'),server)
    recv_msg = sk.recv(1024).decode('utf-8')
    if recv_msg.upper() == 'Q': break
    print(recv_msg)
```



# 3.基于tcp协议完成一个文件的上传

```
    小文件
    进阶 大文件
```
## 小文件上传

**server**

```python
import socket

path=r'D:\2.txt'

sk = socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()
conn,addr = sk.accept()

b = conn.recv(1024)
with open(path,mode='wb') as f:
    f.write(b)
conn.send('文件接收成功！'.encode('utf-8'))
conn.close()

sk.close()
```

**client**

```python
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9001))

path=r'D:\1.txt'
with open(path, mode='rb') as f:
    b=f.read()
sk.send(b)
recv_msg = sk.recv(1024)
print(recv_msg.decode('utf-8'))

sk.close()
```

## 大文件上传（已整合老师答案）

**server**

```python
import json
import struct
import socket

def myrecv():
    blen_obj_bytes=conn.recv(4)
    len_obj_bytes=struct.unpack('i',blen_obj_bytes)[0]
    obj_bytes=conn.recv(len_obj_bytes)
    obj=json.loads(obj_bytes.decode('utf-8'))
    return obj

sk = socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()

conn,_ =sk.accept()

fileinfo_dic=myrecv()

with open(fileinfo_dic['filename'],'wb') as f:
    while fileinfo_dic['filesize'] > 0:
        content = conn.recv(1024)
        fileinfo_dic['filesize'] -= len(content)    #当收取的内容比较大时，tcp协议的优化机制可能会自动帮你解包，把大的数据拆分成若干个小块，因此每次收到的不一定是1024，可能会比1024小，因此这里-=len(content)，而不是-=1024
        f.write(content)
conn.close()
sk.close()
```

**client**

```python
import os
import json
import struct
import socket

def mysend(obj):
    obj_bytes = json.dumps(obj).encode('utf-8')
    blen_obj_bytes = struct.pack('i',len(obj_bytes))
    sk.send(blen_obj_bytes)
    sk.send(obj_bytes)

sk = socket.socket()
sk.connect(('127.0.0.1',9001))

path = r'D:\1.mp4'
filename = os.path.basename(path)
filesize = os.path.getsize(path)
fileinfo_dic = {'filename':filename,'filesize':filesize}     #一般使用字典保存文件名和文件大小

mysend(fileinfo_dic)

with open(path,mode = 'rb') as f:
    while filesize>0:
        content = f.read(1024)
        filesize -= len(content)    #为了和server.py保持一致，这里也写成len。由于客户端读文件时不存在自动解包的问题，这里写成-=1024也行。
        sk.send(content)

print('文件上传完毕！')
sk.close()
```

# 4. 【补充】基于tcp协议完成一个文件的下载

## 大文件下载

**server**

```python
import json
import struct
import socket
import os

def mysend(obj):
    obj_bytes = json.dumps(obj).encode('utf-8')
    blen_obj_bytes = struct.pack('i',len(obj_bytes))
    conn.send(blen_obj_bytes)
    conn.send(obj_bytes)

def myrecv():
    blen_obj_bytes=conn.recv(4)
    len_obj_bytes=struct.unpack('i',blen_obj_bytes)[0]
    obj_bytes=conn.recv(len_obj_bytes)
    obj=json.loads(obj_bytes.decode('utf-8'))
    return obj

sk = socket.socket()
sk.bind(('127.0.0.1',9017))
sk.listen()
conn,_ =sk.accept()

dirpath=r'D:\软件'
file_list=os.listdir(dirpath)
for i in range(len(file_list)):
    file_list[int(i)]=os.path.join(dirpath,file_list[i])

mysend(file_list)
download_num=myrecv()

filepath = file_list[download_num-1]
filename = os.path.basename(filepath)
filesize = os.path.getsize(filepath)
fileinfo_dic = {'filename':filename,'filesize':filesize}

mysend(fileinfo_dic)

with open( filepath, mode = 'rb') as f:
    while filesize>0:
        content = f.read(1024)
        filesize -= len(content)
        conn.send(content)

print('文件传输完毕！')
conn.close()
sk.close()
```

**client**

```python
import os
import json
import struct
import socket

def mysend(obj):
    obj_bytes = json.dumps(obj).encode('utf-8')
    blen_obj_bytes = struct.pack('i',len(obj_bytes))
    sk.send(blen_obj_bytes)
    sk.send(obj_bytes)

def myrecv():
    blen_obj_bytes=sk.recv(4)
    len_obj_bytes=struct.unpack('i',blen_obj_bytes)[0]
    obj_bytes=sk.recv(len_obj_bytes)
    obj=json.loads(obj_bytes.decode('utf-8'))
    return obj

sk = socket.socket()
sk.connect(('127.0.0.1',9017))

file_list=myrecv()

for index,item in enumerate(file_list,1):
    print(index,item)
download_num=int(input('请输入要下载的文件序号>>>').strip())

mysend(download_num)
fileinfo_dic=myrecv()

with open(fileinfo_dic['filename'],'wb') as f:
    while fileinfo_dic['filesize'] > 0:
        content = sk.recv(1024)
        fileinfo_dic['filesize'] -= len(content)
        f.write(content)

print('文件下载完毕！')
sk.close()
```

# 5.选课系统作业

已完成，请见《第六次周末大作业：学生选课系统、面向对象思维导图、博客园》