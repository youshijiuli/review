#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   index.py
@Author  :   cat 
@Version :   3.10
"""
import copy

a = [1, 2, 3, [4, 5], 6]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
b.append(10)
c[3].append(11)
d[3].append(12)

print(a)
print(b)
print(c)
print(d)

# [1, 2, 3, [4, 5,11], 6,10]
# [1, 2, 3, [4, 5,11], 6,10]
# [1, 2, 3, [4, 5,11], 6]
# [1, 2, 3, [4, 5,12], 6]


print('==================')

# l1 = [1,[2],'tree']
# print(l1)

# l2 = l1.copy()
# # print(l2)
# # print(id(l1),id(l2))

# # [1, [2], 'tree']
# # [1, [2], 'tree']
# # 1248669925248 1248669924928

# l2[0] = 'one'
# print(l2)
# print(l1)

# l2[1][0] = 'two'
# print(l2)
# print(l1)

# # [1, [2], 'tree']
# # ['one', [2], 'tree']
# # [1, [2], 'tree']
# # ['one', ['two'], 'tree']
# # [1, ['two'], 'tree']


# 就是不止拷贝指针，连对象也会拷贝，创建出来一份新的，完全独立
l = [1, [2], 'three']
print(l)

from copy import deepcopy

l2 = deepcopy(l)
print(l2)

# 修改新列表不会影响旧列表
l2[1][0] = 'two'
print(l2)
print(l)
# [1, [2], 'three']
# [1, [2], 'three']
# [1, ['two'], 'three']
# [1, [2], 'three']