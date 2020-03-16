#!/usr/bin/env python3
"""
###############################################################################
import random

def guess_number(n):

    guesstokens = 0

    r = random.randint(1, 100)

    print('Guess a number between 1 and 100 ')

    while guesstokens < 101 :


        x = int(input())

        if x == n:
            print('WIN')
            return
        elif x < n:
            print('Guess is too low')
            guesstokens += 1
        else:
            print('Guess is too high')
            guesstokens += 1

guess_number(23)
###############################################################################
"""


def guess_number(n):
    while True:
        guess = int(input('Enter an integer: '))
        if guess == n:
            print('WIN')
            break
        elif guess < n:
            print('TOO LOW')
        else:
            print('TOO HIGH')

guess_number(23)
