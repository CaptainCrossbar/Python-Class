#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice10.py
# Author : CaptainCrossbar
# Creation Date : 12 - March - 2020
# Last Modified : 12 - March - 2020
# Description :
#
###############################################################################
"""

'''
Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.
'''

str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for x in str1:
    if x in freq.keys():
        freq[x] += 1
    else:
        freq[x] = 1
