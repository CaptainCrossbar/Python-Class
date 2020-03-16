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
Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
'''

with open('school_prompt.txt') as fp:
    three = []
    for line in fp:
        three.append(line.split()[2])
