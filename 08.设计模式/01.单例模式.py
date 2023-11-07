#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   01.单例模式.py
@Author  :   cat 
@Version :   3.10
'''

# 1.python实现单例模式（2种方法）


class Person(object):
    """docstring for Person."""
    def __init__(self, arg):
        super(Person, self).__init__()
        self.arg = arg

    def __enter__(self):
        return self
    
    def __exit__(*exc_info):
        return 999
    
p = Person(666)