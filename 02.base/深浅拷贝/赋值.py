# 赋值
'''
就是将对象与变量名字进行绑定，称为名字绑定
在 Python 中，变量只是一个与实际对象绑定起来的名字，变量定义本质上就是建立名字与对象的约束关系。因此，赋值语句本质上就是建立这样的约束关系，将右边的对象与左边的名字绑定在一起：

a = 1
我经常在面试中问：除了赋值语句，还有哪些语句可以完成名字绑定？

1. 模块导入
我们导入模块时，也会在当前上下文创建一个名字，并与被导入对象绑定：

import xxx
from xxx import yyy
2. 函数类定义
我们定义函数/类时，本质上是创建了一个函数/类对象，然后将其与函数/类名绑定：

def circle_area(r):
    return PI * r ** 2

class Dog(object):
    pass

3. as 关键字
除此此外， as 关键字也可以在当前上下文建立名字约束关系：

import xxx as yyy
from xxx import yyy as zzz

with open('/some/file') as f:
    pass

try:
    # do something
except SomeError as e:
    # handle error
'''