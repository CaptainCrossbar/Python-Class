#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : practice13.py
# Author : CaptainCrossbar
# Creation Date : 12 - March - 2020
# Last Modified : 12 - March - 2020
# Description :
#
###############################################################################
"""

'''
Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.
'''

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d = {}
send = sent.split()
for w in send:
    wrd_d[w] = wrd_d.get(w, 0) + 1
