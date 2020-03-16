#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice6.py
# Author : CaptainCrossbar
# Creation Date : 11 - March - 2020
# Last Modified : 11 - March - 2020
# Description :
#
###############################################################################
"""

'''
Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
'''

with open('emotion_words.txt') as fp:
    emotions = []
    for line in fp:
        emotions.append(line.split()[0])
