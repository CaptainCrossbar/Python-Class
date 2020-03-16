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
The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
Find the total number of characters in the file and save to the variable num.
'''

with open('travel_plans.txt') as fp:
    data = fp.read()
    num = len(data)
