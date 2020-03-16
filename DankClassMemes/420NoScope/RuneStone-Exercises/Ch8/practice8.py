#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice8.py
# Author : CaptainCrossbar
# Creation Date : 11 - March - 2020
# Last Modified : 11 - March - 2020
# Description :
#
###############################################################################
"""

'''
Write code so that if "STATS 250" is in the list schedule, then the string "You could be in Information Science!" is assigned to the variable resp.
Otherwise, the string "That's too bad." should be assigned to the variable resp.
'''

schedule = ["SI 106", "STATS 250", "SI 110", "ENGLISH 124/125"]

if 'STATS 250' in schedule:
    resp = 'You could be in Information Science!'
else:
    resp = 'Thats too bad.'
