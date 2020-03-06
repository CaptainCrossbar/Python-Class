#!/usr/bin/env python3

import random

"""
###############################################################################
#
# File Name : randomnum.py
# Author : 2LT PWB
# Creation Date : 05 - March - 2020
# Last Modified : 06 - March - 2020
# Description : Creates a random number and checks it against some preconfigured checks
#
###############################################################################
"""

def main():

    r = random.randint(1, 1000)
    
    if r == 69:
        print('Ayyyyy, my mans. Thats hot')
    elif r == 420:
        print('You won the lottery and just scored yourself a, air quotes, random UA')
    else:
        print((r), 'Better luck next time champ. I just mugged you off bruv', sep':')

if __name__ == "__main__":
    main()
