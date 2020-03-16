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
Create one conditional so that if “Friendly” is in w, then “Friendly is here!” should be assigned to the variable wrd.
If it’s not, check if “Friend” is in w. If so, the string “Friend is here!” should be assigned to the variable wrd,
otherwise “No variation of friend is in here.” should be assigned to the variable wrd.
(Also consider: does the order of your conditional statements matter for this problem? Why?)
'''

w = "Friendship is a wonderful human experience!"
wrd = ''
if w.find('Friendly') != -1:
    wrd += 'Friendly is here!'
elif w.find('Friend') != -1:
    wrd += 'Friend is here!'
else:
    wrd += 'No variation of friend is in here'
