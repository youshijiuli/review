**day27作业（张珵）**

**用反射完成：**

**python xx.py oddgod 123 cp path1 path2**
**python xx.py oddgod 123 rm path**
**python xx,py oddgod 123 mv path1 path2**

python xx,py oddgod 123 rn path1 path2

python xx,py oddgod 123 mkdir path

......

**类比day22作业的sys.argv练习**

```python
# 方法一：用面向对象做
# 注意sys.argv[]索引号是从0开始的

import sys
import os
import shutil

class File(object):

    def __init__(self,path1,path2=None):
        self.path1 = path1
        self.path2 = path2

    def cp(self):
        '''
        cp：将一个文件复制到一个已存在的文件夹，注意若文件夹不存在则不能直接copy2，否则报错！
        :return:
        '''
        if len(sys.argv) == 6:
            if os.path.exists(self.path1) and os.path.exists(self.path2):
                path = os.path.join(self.path2, os.path.basename(self.path1))
                shutil.copy2(self.path1, path)

    def rm(self):
        '''
        删除一个文件或文件夹
        :return:
        '''
        if len(sys.argv) == 5:
            if os.path.exists(self.path1):
                if os.path.isfile(self.path1):
                    os.remove(self.path1)
                else:
                    shutil.rmtree(self.path1)

    def rn(self):
        '''
        将一个文件或文件夹重命名
        :return:
        '''
        if len(sys.argv) == 6:
            if os.path.exists(self.path1):
                os.rename(self.path1, self.path2)

    def mv(self):
        '''
        将一个文件移动到一个已存在的文件夹
        :return:
        '''
        if len(sys.argv) == 6:
            if os.path.exists(self.path1) and os.path.exists(self.path2):
                path = os.path.join(self.path2, os.path.basename(self.path1))
                shutil.move(self.path1, path, copy_function=shutil.copy2)

    def mkdir(self):
        '''
        新建一个文件夹
        :return:
        '''
        if len(sys.argv) == 5:
            if not os.path.exists(self.path1):
                os.mkdir(self.path1)

#主程序
if 5<=len(sys.argv)<=6:
    if sys.argv[1] == 'oddgod' and sys.argv[2] == '123':

        if len(sys.argv) == 5:
            f = File(sys.argv[4])
        elif len(sys.argv) == 6:
            f = File(sys.argv[4], sys.argv[5])

        if hasattr(f, sys.argv[3]) and callable(getattr(f, sys.argv[3])):
            getattr(f, sys.argv[3])()
        else:
            print('指令输入错误')
    else:
        print('用户名或密码错误！')
else:
    print('您输入的命令长度不足')
```

```python
# 方法二：不用面向对象做
# 注意sys.argv[]索引号是从0开始的

import sys
import os
import shutil

def cp():
    '''
    cp：将一个文件复制到一个已存在的文件夹，注意若文件夹不存在则不能直接copy2，否则报错！
    :return:
    '''
    if len(sys.argv) == 6:
        if os.path.exists(sys.argv[4]) and os.path.exists(sys.argv[5]):
            path = os.path.join(sys.argv[5], os.path.basename(sys.argv[4]))
            shutil.copy2(sys.argv[4], path)

def rm():
    '''
    删除一个文件或文件夹
    :return:
    '''
    if len(sys.argv) == 5:
        if os.path.exists(sys.argv[4]):
            if os.path.isfile(sys.argv[4]):
                os.remove(sys.argv[4])
            else:
                shutil.rmtree(sys.argv[4])

def rn():
    '''
    将一个文件或文件夹重命名
    :return:
    '''
    if len(sys.argv) == 6:
        if os.path.exists(sys.argv[4]):
            os.rename(sys.argv[4], sys.argv[5])

def mv():
    '''
    将一个文件移动到一个已存在的文件夹
    :return:
    '''
    if len(sys.argv) == 6:
        if os.path.exists(sys.argv[4]) and os.path.exists(sys.argv[5]):
            path = os.path.join(sys.argv[5], os.path.basename(sys.argv[4]))
            shutil.move(sys.argv[4], path, copy_function=shutil.copy2)

def mkdir():
    '''
    新建一个文件夹
    :return:
    '''
    if len(sys.argv) == 5:
        if not os.path.exists(sys.argv[4]):
            os.mkdir(sys.argv[4])

#主程序
if len(sys.argv) >= 5:
    if sys.argv[1] == 'oddgod' and sys.argv[2] == '123':
        if hasattr(sys.modules['__main__'],sys.argv[3]) and callable(getattr(sys.modules['__main__'],sys.argv[3])):
            getattr(sys.modules['__main__'],sys.argv[3])()
        else:
            print('输入错误！')
    else:
        print('用户名或密码错误！')
else:
    print('您输入的命令长度不足')
```