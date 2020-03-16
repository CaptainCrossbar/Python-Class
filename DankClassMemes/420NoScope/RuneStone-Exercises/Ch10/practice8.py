#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice1.py
# Author : CaptainCrossbar
# Creation Date : 11 - March - 2020
# Last Modified : 11 - March - 2020
# Description :
#
###############################################################################
"""

'''
Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
'''

with open('school_prompt.txt') as fp:
    p_words = []
    for line in fp:
        for word in line.split():
            if 'p' in word:
                p_words.append(word)
