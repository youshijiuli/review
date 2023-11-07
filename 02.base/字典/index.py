#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   index.py
@Author  :   Cat 
@Version :   3.11
"""


# 字典赋值的坑
l = []
for i in range(10):
    l.append({"num": i})

print(l)


k = []
a = {"num": 0}
for i in range(10):
    a["num"] = i
    k.append(a)

print(k)

# [{'num': 0}, {'num': 1}, {'num': 2}, {'num': 3}, {'num': 4}, {'num': 5}, {'num': 6}, {'num': 7}, {'num': 8}, {'num': 9}]
# [{'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}, {'num': 9}]