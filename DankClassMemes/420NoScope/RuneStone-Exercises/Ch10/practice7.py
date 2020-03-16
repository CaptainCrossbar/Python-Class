#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice7.py
# Author : CaptainCrossbar
# Creation Date : 11 - March - 2020
# Last Modified : 11 - March - 2020
# Description :
#
###############################################################################
"""

'''
Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
'''

with open('travel_plans.txt') as fp:
    first_chars = fp.read()[:33]
