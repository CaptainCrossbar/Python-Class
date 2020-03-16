#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice2.py
# Author : CaptainCrossbar
# Creation Date : 11 - March - 2020
# Last Modified : 11 - March - 2020
# Description :
#
###############################################################################
"""

'''
We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
Find the total number of words in the file and assign this value to the variable num_words.
'''

with open('emotion_words.txt') as fp:
    data = fp.read()
    words = data.split()
    num_words = len(words)
