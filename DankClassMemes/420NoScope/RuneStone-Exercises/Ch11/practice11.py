#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice11.py
# Author : CaptainCrossbar
# Creation Date : 12 - March - 2020
# Last Modified : 12 - March - 2020
# Description :
#
###############################################################################
"""

'''
Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.
'''

s1 = "hello"
counts = {}
for c in s1:
    counts[c] = counts.get(c, 0) + 1
