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
