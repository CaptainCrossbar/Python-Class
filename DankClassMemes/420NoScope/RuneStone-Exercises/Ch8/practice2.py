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
The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words.
Store the result in the variable same_letter_count.
'''

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
same_letter_count = 0
words = sentence.split()
for x in words:
    if x[0] == x[-1]:
        same_letter_count += 1
