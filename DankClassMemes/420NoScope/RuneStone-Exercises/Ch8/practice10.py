#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice10.py
# Author : CaptainCrossbar
# Creation Date : 11 - March - 2020
# Last Modified : 11 - March - 2020
# Description :
#
###############################################################################
"""

'''
For each string in wrd_lst, find the number of characters in the string.
If the number of characters is less than 6, add 1 to accum so that in the end,
accum will contain an integer representing the total number of words in the list that have fewer than 6 characters.
'''

wrd_lst = ["Hello", "activecode", "Java", "C#", "Python", "HTML and CSS", "Javascript", "Swift", "php"]

accum = 0
for x in wrd_lst:
    v = len(x)
    if v < 6:
        accum += 1
