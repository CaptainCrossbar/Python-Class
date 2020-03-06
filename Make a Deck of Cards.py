def makedeck():
  #list of the suits
  suits = ['\u2660','\u2665','\u2666','\u2663']
  #list of the cards in a suit
  ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
  #creates the deck
  deck = ['{}{}'.format(rank,suit) for suit in suits for rank in ranks]
  #prints the deck out
  print(deck)
  return makedeck

makedeck()
