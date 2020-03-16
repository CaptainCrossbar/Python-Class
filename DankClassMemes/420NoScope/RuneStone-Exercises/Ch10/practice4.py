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
Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
'''

with open('school_prompt.txt') as fp:
    beginning_chars = fp.read()[:30]
