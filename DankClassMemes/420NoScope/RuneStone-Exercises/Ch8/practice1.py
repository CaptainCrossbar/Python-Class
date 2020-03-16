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
rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma.
Write code to compute the number of months that have more than 3 inches of rainfall.
Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0
'''

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rain = rainfall_mi.split(',')
num_rainy_months = 0
for inches in rain:
    if float(inches) > 3:
        num_rainy_months += 1
