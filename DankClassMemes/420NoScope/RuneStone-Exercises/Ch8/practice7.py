#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice7.py
# Author : CaptainCrossbar
# Creation Date : 11 - March - 2020
# Last Modified : 11 - March - 2020
# Description :
#
###############################################################################
"""

'''
We have written conditionals for you to use.
Create the variable x and assign it some integer so that at the end of the code, output will be assigned the string "Consistently working".
'''

x = 9
if x >= 10:
    output = "working"
else:
    output = "Still working"
if x > 12:
    output = "Always working"
elif x < 7:
    output = "Forever working"
else:
    output = "Consistently working"
