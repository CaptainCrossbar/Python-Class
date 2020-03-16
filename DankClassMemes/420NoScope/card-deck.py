#!/usr/bin/env python3

"""
###############################################################################
#
# File Name : card-deck.py
# Author : CaptainCrossbar
# Creation Date : 10 - March - 2020
# Last Modified : 10 - March - 2020
# Description : Makes a deck of cards
#
###############################################################################
"""

def makedeck():
  suits = ['\u2660','\u2665','\u2666','\u2663']
  ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
  deck = ['{}{}'.format(rank,suit) for suit in suits for rank in ranks]
  print(deck)
  return makedeck

makedeck()
