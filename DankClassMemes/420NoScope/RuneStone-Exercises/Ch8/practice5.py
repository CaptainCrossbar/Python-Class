#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice5.py
# Author : CaptainCrossbar
# Creation Date : 11 - March - 2020
# Last Modified : 11 - March - 2020
# Description :
#
###############################################################################
"""

'''
Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels.
For this problem, vowels are only a, e, i, o, and u.
Hint: use the in operator with vowels.
'''

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

num_vowels = 0
for vowels in vowels:
    num_vowels += s.count(vowels)
