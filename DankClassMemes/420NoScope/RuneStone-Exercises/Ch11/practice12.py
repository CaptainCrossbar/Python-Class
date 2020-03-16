#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice12.py
# Author : CaptainCrossbar
# Creation Date : 12 - March - 2020
# Last Modified : 12 - March - 2020
# Description :
#
###############################################################################
"""

'''
Create a dictionary, freq_words, that displays each word in string str1 as the key and its frequency as the value.
'''

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
strng = str1.split()
freq_words = {}
for x in strng:
    freq_words[x] = freq_words.get(x, 0) + 1
