#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : decorator.py
# Author :CaptainCrossbar
# Creation Date : 10 - March - 2020
# Last Modified : 12 - March - 2020
# Description : Makes a basic decorator
#
###############################################################################
"""

import time

def profile(func):
    def profile_inner(*args,**kwargs):
        begin = time.perf_counter()
        func(*args,**kwargs)
        print('{} took {}s'.format(func.__name__,time.perf_counter()-begin))
    return profile_inner

@profile
def calc():
    time.sleep(5)

@profile
def calc2():
    time.sleep(2)

if __name__ == '__main__':
    calc()
    calc2()
