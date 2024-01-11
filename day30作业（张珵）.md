# day30作业

1.登录 + 文件下载
    用户必须登录才能下载
    用户是否登录应该记录在服务器
    并且用户可以自己选择 上传 还是 下载
2.用socketserver实现上面的题

# 第一题（socket）（张珵原始版，无反射）

### server

```python
import socket
import struct
import json
import os

path=r'D:\My Documents\Pycharm\data'

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
sk.bind(('127.0.0.1',9001))
sk.listen()

while True:
    conn,_ = sk.accept()
    status=False

    while status==False:
        input_username=myrecv()
        input_cipertext=myrecv()
        with open(path,encoding='utf-8') as f1:
            for line in f1:
                username, cipertext = line.strip().split('|')
                if input_username == username and input_cipertext == cipertext:
                    status=True
                    break
            else:
                status=False
        mysend(status)

    while True:
        choice = myrecv()
        if choice == '1':
            fileinfo_dic = myrecv()
            with open(fileinfo_dic['filename'], 'wb') as f2:
                while fileinfo_dic['filesize'] > 0:
                    content = conn.recv(1024)
                    fileinfo_dic['filesize'] -= len(content)
                    f2.write(content)
            print('用户成功上传了文件%s'%(fileinfo_dic['filename']))
        if choice == '2':
            dirpath = r'D:\软件'
            file_list = os.listdir(dirpath)
            for i in range(len(file_list)):
                file_list[int(i)] = os.path.join(dirpath, file_list[i])
            mysend(file_list)
            download_num = myrecv()
            filepath = file_list[download_num - 1]
            filename = os.path.basename(filepath)
            filesize = os.path.getsize(filepath)
            fileinfo_dic = {'filename': filename, 'filesize': filesize}
            mysend(fileinfo_dic)
            with open(filepath, mode='rb') as f:
                while filesize > 0:
                    content = f.read(1024)
                    filesize -= len(content)
                    conn.send(content)
            print('用户成功下载了文件%s' % (filename))
        if choice == '3':
            conn.close()
            break
```

## client

```python
import socket
import struct
import hashlib
import json
import os

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

def encrypt(username,password):
    md5=hashlib.md5(username.encode('utf-8'))
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

sk = socket.socket()
sk.connect(('127.0.0.1',9001))
status=False

while status==False:
    username=input('请输入用户名>>>').strip()
    password=input('请输入密码>>>').strip()
    cipertext=encrypt(username,password)
    mysend(username)
    mysend(cipertext)
    status=myrecv()
    if status==False:
        print('用户名或密码错误，请重新登陆！')
print('登陆成功!')
option_list = [('上传', 'upload'), ('下载', 'download'), ('退出','exit')]
while True:
    for index, item in enumerate(option_list,1):
        print(index, item[0])
    choice = input('请输入您的选项>>>').strip()
    mysend(choice)
    if choice=='1':
        filepath = input('请输入要上传文件的绝对路径>>>').strip()
        if os.path.isfile(filepath):
            filename = os.path.basename(filepath)
            filesize = os.path.getsize(filepath)
            fileinfo_dic = {'filename': filename, 'filesize': filesize}
            mysend(fileinfo_dic)
            with open(filepath, mode='rb') as f:
                while filesize > 0:
                    content = f.read(1024)
                    filesize -= len(content)
                    sk.send(content)
            print('文件上传完毕！')
        else:
            print('指定路径的文件不存在！')
    elif choice=='2':
        file_list = myrecv()
        for index, item in enumerate(file_list, 1):
            print(index, item)
        download_num = int(input('请输入要下载的文件序号>>>').strip())
        mysend(download_num)
        fileinfo_dic = myrecv()
        with open(fileinfo_dic['filename'], 'wb') as f:
            while fileinfo_dic['filesize'] > 0:
                content = sk.recv(1024)
                fileinfo_dic['filesize'] -= len(content)
                f.write(content)
        print('文件下载完毕！')
    elif choice=='3':
        print('系统退出')
        sk.close()
        break
    else:
        print('您的输入有误，请检查后重新输入')
```

## data

```
用户名|用户名为盐的密码123456的密文
tom|f19b50d5e3433e65e6879d0e66632664
jerry|496e242f69ba941cd1bc5b2732469c11
oddgod|3bc6354368b25733dacd34fc254367ca
```



# 第一题（socket）（基于老师版改良，带反射）

## server

```python
import os
import sys
import json
import struct
import socket
import hashlib

userinfo_path=r'userinfo'

def get_md5(salt,text):
    md5 = hashlib.md5(salt.encode('utf-8'))
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()

def get_sha1(salt,text):
    sha1 = hashlib.sha1(salt.encode('utf-8'))
    sha1.update(text.encode('utf-8'))
    return sha1.hexdigest()

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

def login(conn):
    flag = True
    while flag:
        login_form_dic = myrecv(conn)
        with open(userinfo_path, encoding='utf-8') as f:
            for line in f:
                username, cipertext = line.strip().split('|')
                if username == login_form_dic['username'] and cipertext == get_sha1(username, login_form_dic['password_md5']):
                    login_result = True
                    flag = False
                    break
            else:
                login_result = False
            login_result_dic = {'operate': 'login', 'result': login_result}
            mysend(conn, login_result_dic)

def upload(conn,opt_dic):
    with open(opt_dic['filename'], 'wb') as f:
        while opt_dic['filesize'] > 0:
            content = conn.recv(1024)
            opt_dic['filesize'] -= len(content)
            f.write(content)

def download(conn,opt_dic):
    filepath = r'D:\1.mp4'
    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)
    fileinfo_dic = {'filename': filename, 'filesize': filesize}
    mysend(conn,fileinfo_dic)
    with open(filepath, mode='rb') as f:
        while filesize > 0:
            content = f.read(1024)
            filesize -= len(content)
            conn.send(content)

sk = socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()
conn,_ =sk.accept()
login(conn)
opt_dic = myrecv(conn)
if hasattr(sys.modules[__name__],opt_dic['operate']):
    getattr(sys.modules[__name__],opt_dic['operate'])(conn,opt_dic)
conn.close()
sk.close()
```

## client

```python
import os
import sys
import json
import struct
import socket
import hashlib

def get_md5(salt,text):
    md5 = hashlib.md5(salt.encode('utf-8'))
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()

def mysend(sk,obj):
    bobj = json.dumps(obj).encode('utf-8')
    blen_bobj = struct.pack('i',len(bobj))
    sk.send(blen_bobj)
    sk.send(bobj)

def myrecv(sk):
    blen_bobj=sk.recv(4)
    len_bobj=struct.unpack('i',blen_bobj)[0]
    bobj=sk.recv(len_bobj)
    obj=json.loads(bobj.decode('utf-8'))
    return obj

def login(sk):
    while True:
        username = input('请输入用户名>>>').strip()
        password = input('请输入密码>>>').strip()
        if username and password:
            password_md5=get_md5(username,password)
            login_form_dic = {'username': username, 'password_md5': password_md5}
            mysend(sk, login_form_dic)
            login_result_dic = myrecv(sk)
            if login_result_dic['operate'] == 'login' and login_result_dic['result']:
                print('登录成功')
                break
            else:
                print('登录失败')
        else:
            print('用户名和密码均不能为空！')

def upload(sk):
    filepath = r'D:\1.mp4'
    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)
    opt_dic = {'operate': 'upload','filename':filename,'filesize':filesize}
    mysend(sk, opt_dic)
    with open(filepath, mode='rb') as f:
        while filesize > 0:
            content = f.read(1024)
            filesize -= len(content)
            sk.send(content)
    print('上传完毕')

def download(sk):
    # 这里可以加入别的信息，比如要下载哪个文件？
    opt_dic = {'operate':'download'}
    mysend(sk,opt_dic)
    fileinfo_dic = myrecv(sk)
    with open(fileinfo_dic['filename'], 'wb') as f:
        while fileinfo_dic['filesize'] > 0:
            content = sk.recv(1024)
            fileinfo_dic['filesize'] -= len(content)
            f.write(content)
    print('下载完毕')

def exit(sk):
    print('Bye!')
    return False

sk = socket.socket()
sk.connect(('127.0.0.1',9001))
opt_tuple_list = [
    ('上传文件','upload'),
    ('下载文件','download'),
    ('退出程序','exit')]
login(sk)
while True:
    for index,opt_tuple in enumerate(opt_tuple_list,1):
        print(index,opt_tuple[0])
    opt_num = input('请选择您要操作的序号>>>').strip()
    if opt_num.isdecimal():
        opt_num = int(opt_num)
        if 1 <= opt_num <= len(opt_tuple_list):
            flag = getattr(sys.modules[__name__], opt_tuple_list[opt_num-1][1])(sk)
            if flag=='exit':
                break
        else:
            print('您输入的序号超出范围，请重新输入！')
    else:
        print('您输入的序号含有非法字符，请重新输入！')
sk.close()



```



# 第二题（socketserver并发）（张珵原始版，无反射）

## server

```python
import struct
import json
import os
import socketserver

path=r'D:\My Documents\Pycharm\data'

class Myserver(socketserver.BaseRequestHandler):

    @staticmethod
    def mysend(conn,obj):
        bobj = json.dumps(obj).encode('utf-8')
        blen_bobj = struct.pack('i', len(bobj))
        conn.send(blen_bobj)
        conn.send(bobj)

    @staticmethod
    def myrecv(conn):
        blen_bobj = conn.recv(4)
        len_bobj = struct.unpack('i', blen_bobj)[0]
        bobj = conn.recv(len_bobj)
        obj = json.loads(bobj.decode('utf-8'))
        return obj

    def handle(self):

        conn = self.request

        flag=True

        while flag:

            status=False

            while status==False:
                input_username=self.myrecv(conn)
                input_cipertext=self.myrecv(conn)
                with open(path,encoding='utf-8') as f1:
                    for line in f1:
                        username, cipertext = line.strip().split('|')
                        if input_username == username and input_cipertext == cipertext:
                            status=True
                            break
                    else:
                        status=False
                self.mysend(conn,status)

            while True:
                choice = self.myrecv(conn)
                if choice == '1':
                    fileinfo_dic = self.myrecv(conn)
                    with open(fileinfo_dic['filename'], 'wb') as f2:
                        while fileinfo_dic['filesize'] > 0:
                            content = conn.recv(1024)
                            fileinfo_dic['filesize'] -= len(content)
                            f2.write(content)
                    print('用户%s成功上传了文件%s'%(username,fileinfo_dic['filename']))
                if choice == '2':
                    dirpath = r'D:\软件'
                    file_list = os.listdir(dirpath)
                    for i in range(len(file_list)):
                        file_list[int(i)] = os.path.join(dirpath, file_list[i])
                    self.mysend(conn,file_list)
                    download_num = self.myrecv(conn)
                    filepath = file_list[download_num - 1]
                    filename = os.path.basename(filepath)
                    filesize = os.path.getsize(filepath)
                    fileinfo_dic = {'filename': filename, 'filesize': filesize}
                    self.mysend(conn,fileinfo_dic)
                    with open(filepath, mode='rb') as f:
                        while filesize > 0:
                            content = f.read(1024)
                            filesize -= len(content)
                            conn.send(content)
                    print(f'用户{username}成功下载了文件{filename}')
                if choice == '3':
                    print(f'用户{username}退出')
                    conn.close()
                    flag=False
                    break

server = socketserver.ThreadingTCPServer(('127.0.0.1',9001),Myserver)
server.serve_forever()
```

## client

```python
import socket
import struct
import hashlib
import json
import os

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

def encrypt(username,password):
    md5=hashlib.md5(username.encode('utf-8'))
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

sk = socket.socket()
sk.connect(('127.0.0.1',9001))
status=False

while status==False:
    username=input('请输入用户名>>>').strip()
    password=input('请输入密码>>>').strip()
    cipertext=encrypt(username,password)
    mysend(username)
    mysend(cipertext)
    status=myrecv()
    if status==False:
        print('用户名或密码错误，请重新登陆！')
print('登陆成功!')
option_list = [('上传', 'upload'), ('下载', 'download'), ('退出','exit')]
while True:
    for index, item in enumerate(option_list,1):
        print(index, item[0])
    choice = input('请输入您的选项>>>').strip()
    mysend(choice)
    if choice=='1':
        filepath = input('请输入要上传文件的绝对路径>>>').strip()
        if os.path.isfile(filepath):
            filename = os.path.basename(filepath)
            filesize = os.path.getsize(filepath)
            fileinfo_dic = {'filename': filename, 'filesize': filesize}
            mysend(fileinfo_dic)
            with open(filepath, mode='rb') as f:
                while filesize > 0:
                    content = f.read(1024)
                    filesize -= len(content)
                    sk.send(content)
            print('文件上传完毕！')
        else:
            print('指定路径的文件不存在！')
    elif choice=='2':
        file_list = myrecv()
        for index, item in enumerate(file_list, 1):
            print(index, item)
        download_num = int(input('请输入要下载的文件序号>>>').strip())
        mysend(download_num)
        fileinfo_dic = myrecv()
        with open(fileinfo_dic['filename'], 'wb') as f:
            while fileinfo_dic['filesize'] > 0:
                content = sk.recv(1024)
                fileinfo_dic['filesize'] -= len(content)
                f.write(content)
        print('文件下载完毕！')
    elif choice=='3':
        print('系统退出')
        # sk.close()
        break
    else:
        print('您的输入有误，请检查后重新输入')
```

## data

```
用户名|用户名为盐的密码123456的密文
tom|f19b50d5e3433e65e6879d0e66632664
jerry|496e242f69ba941cd1bc5b2732469c11
oddgod|3bc6354368b25733dacd34fc254367ca
```