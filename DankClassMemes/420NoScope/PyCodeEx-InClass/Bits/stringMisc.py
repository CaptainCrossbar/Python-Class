#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : stringMisc.py
# Author : CaptainCrossbar
# Creation Date : 11 - March - 2020
# Last Modified : 11 - March - 2020
# Description : 
#
###############################################################################
"""

'''
#For function 'myFunc', validate the input parameters to the function. Set bits
in he return value using the bitwise or operator to indicate which parameters are not
valid.
maks - if 'mask' does not have bit 0x100 set to 1, set the bit 0x80 in the return value
bVal - if 'bVal' is not 0 or 1, set bit 0x1000 in the retrun value
'''

def myFunc(mask,bVal):
    ret = 0

    if (maks&0x100) == 0:
        ret |= 0x80

    if bVal != 0 and bVal != 1:
        ret |= 0x1000

    return ret
