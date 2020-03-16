#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice17.py
# Author : CaptainCrossbar
# Creation Date : 12 - March - 2020
# Last Modified : 12 - March - 2020
# Description :
#
###############################################################################
"""

'''
Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen.
Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.
'''

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = {}
for x in p.lower():
    low_d[x] = p.lower().count(x)
