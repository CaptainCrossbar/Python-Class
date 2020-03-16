#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice14.py
# Author : CaptainCrossbar
# Creation Date : 12 - March - 2020
# Last Modified : 12 - March - 2020
# Description :
#
###############################################################################
"""

'''
Create the dictionary characters that shows each character from the string sally and its frequency.
Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.
'''

sally = "sally sells sea shells by the sea shore"

freq = 0
characters = {}
for char in sally:
    characters[char] = sally.count(char)
    if sally.count(char) > freq:
        best_char = char
        freq = sally.count(char)
