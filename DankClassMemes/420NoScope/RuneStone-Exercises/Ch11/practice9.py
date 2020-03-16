#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice9.py
# Author : CaptainCrossbar
# Creation Date : 12 - March - 2020
# Last Modified : 12 - March - 2020
# Description :
#
###############################################################################
"""

'''
The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits.
Find the total number of credits taken this semester and assign it to the variable credits. Do not hardcode this – use dictionary accumulation!
'''

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for values in Junior.values():
    credits += values
