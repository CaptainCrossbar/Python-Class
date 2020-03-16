#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice4.py
# Author : CaptainCrossbar
# Creation Date : 11 - March - 2020
# Last Modified : 11 - March - 2020
# Description :
#
###############################################################################
"""

'''
Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.

Note 1: be sure to not double-count words that contain both an a and an e.

HINT 1: Use the in operator.

HINT 2: You can either use or or elif.
'''

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e = 0
for s in sentence.split():
    if 'a' in s or 'e' in s:
        num_a_or_e += 1
