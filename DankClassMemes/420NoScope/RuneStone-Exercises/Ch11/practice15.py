#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice15.py
# Author : CaptainCrossbar
# Creation Date : 12 - March - 2020
# Last Modified : 12 - March - 2020
# Description :
#
###############################################################################
"""

'''
Do the same as above but now find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency.
Then, find the least frequent letter in the string and assign the letter to the variable worst_char.
'''

sally = "sally sells sea shells by the sea shore and by the road"

freq = sally.count(sally[0])
worst_char = sally[0]
characters = {}
for char in sally:
    characters[char] = sally.count(char)
    if sally.count(char) < freq:
        worst_char = char
        freq = sally.count(char)
