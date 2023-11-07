#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   test01.py
@Author  :   cat 
@Version :   3.10
"""


# class Parent(object):
#     x = 1


# class Child1(Parent):
#     pass


# class Child2(Parent):
#     pass


# print(Parent.x, Child1.x, Child2.x)
# # 1  1  1

# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# # 1  2  1

# Child1.x = 3
# print(Parent.x, Child1.x, Child2.x)
# # 1  3  1


print("===================================")


# class A:
#     def func(self):
#         print("A.func")


# class B(A):
#     pass


# class C(A):
#     def func(self):
#         print("C.func")


# class D(B, C):
#     pass


# d = D()
# d.func()
# C.func


class A(object):
    def func(self):
        print("A.func")


class B(A):
    pass


class C(A):
    def func(self):
        print("C.func")


class D(B, C):
    pass


d = D()
d.func()
# C.func
