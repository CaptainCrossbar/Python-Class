#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : test.py
# Author : CaptainCrossbar
# Creation Date : 10 - March - 2020
# Last Modified :
# Description : Makes a basic Generator
#
###############################################################################
"""

def my_gen():
    n = 1
    print('69 is the best')
    yield n

    n += 1
    print('420 Blaze it up')
    yield n

    n += 1
    print('This is the way')
    yield n

for item in my_gen():
    print(item)
