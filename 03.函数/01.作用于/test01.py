#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   test01.py
@Author  :   cat 
@Version :   3.10
"""


a = 1


def func(a):
    a = 2


func(a)

print(a)
# 1

print("==============================")

a = []


def func(a):
    a.append(1)


func(a)
print(a)
# [1]
