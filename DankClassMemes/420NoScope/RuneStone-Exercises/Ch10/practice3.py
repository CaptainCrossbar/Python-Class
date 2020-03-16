#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice3.py
# Author : CaptainCrossbar
# Creation Date : 11 - March - 2020
# Last Modified : 11 - March - 2020
# Description :
#
###############################################################################
"""

'''
Assign to the variable num_lines the number of lines in the file school_prompt.txt.
'''

with open('school_prompt.txt') as fp:
    data = fp.readlines()
    num_lines = len(data)
