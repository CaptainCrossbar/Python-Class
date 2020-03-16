#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice16.py
# Author : CaptainCrossbar
# Creation Date : 12 - March - 2020
# Last Modified : 12 - March - 2020
# Description :
#
###############################################################################
"""

'''
Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1.
Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.
'''

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
string1 = string1.lower()
letter_counts = {}
for c in string1:
    letter_counts[c] = letter_counts.get(c,0) + 1
