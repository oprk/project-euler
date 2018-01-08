# Poker hands
# Problem 54

# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest
# value wins; for example, a pair of eights beats a pair of fives (see example 1
# below). But if two ranks tie, for example, both players have a pair of queens,
# then highest cards in each hand are compared (see example 4 below); if the
# highest cards tie then the next highest cards are compared, and so on.

# Consider the following five hands dealt to two players:

# Hand  Player 1          Player 2            Winner
# 1 	 	5H 5C 6S 7S KD    2C 3S 8S 8D TD      Player 2
#       Pair of Fives     Pair of Eights
# 2 	 	5D 8C 9S JS AC    2C 5C 7D 8S QH      Player 1
#       Highest card Ace  Highest card Queen
# 3 	 	2D 9C AS AH AC    3D 6D 7D TD QD      Player 2
#       Three Aces        Flush with Diamonds
# 4 	 	4D 6S 9H QH QC    3D 6D 7H QD QS      Player 1
#       Pair of Queens    Pair of Queens
#       Highest card Nine Highest card Seven
# 5     2H 2D 4C 4D 4S    3C 3D 3S 9S 9D      Player 1
#       Full House        Full House
#       With Three Fours  with Three Threes

# The file, poker.txt, contains one-thousand random hands dealt to two
# players. Each line of the file contains ten cards (separated by a single
# space): the first five are Player 1's cards and the last five are Player 2's
# cards. You can assume that all hands are valid (no invalid characters or
# repeated cards), each player's hand is in no specific order, and in each hand
# there is a clear winner.

# How many hands does Player 1 win?

from collections import Counter
import csv
import operator

values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suites = ['H', 'S', 'D', 'C']

def hand_suites(hand):
  return [card[1] for card in hand]

def hand_values(hand):
  return [card[0] for card in hand]

def flush(hand):
  return len(set(hand_suites(hand))) == 1

assert flush(['2D', '3D', '4D', '5D', '6D'])
assert not flush(['2H', '3D', '4D', '5D', '6D'])

def royal_flush(hand):
  if not flush(hand):
    return False
  return set(hand_values(hand)) == set(['T', 'J', 'Q', 'K', 'A'])

assert royal_flush(['AH', 'KH', 'QH', 'JH', 'TH'])
assert not royal_flush(['AH', 'KS', 'QH', 'JH', 'TH'])
assert not royal_flush(['AH', '2H', 'QH', 'JH', 'TH'])

def straight(hand):
  order = list(sorted(values.index(value) for value in hand_values(hand)))
  curr = order[0]
  rest = order[1:]
  for elt in rest:
    if elt - curr != 1:
      return False
    curr = elt
  return True

assert straight(['4S', '3H', '2H', '5D', '6C'])

def straight_flush(hand):
  return straight(hand) and flush(hand)

assert straight_flush(['4S', '3S', '2S', '5S', '6S'])
assert not straight_flush(['4S', '3H', '2H', '5D', '6C'])

def four_of_a_kind(hand):
  return Counter(hand_values(hand)).most_common()[0][1] == 4

assert four_of_a_kind(['AH', 'AS', 'AD', 'AC', '2H'])
assert not four_of_a_kind(['AH', 'AS', 'AD', 'TC', '2H'])

def three_of_a_kind(hand):
  most_common = Counter(hand_values(hand)).most_common()
  return (len(most_common) > 2 and
          most_common[0][1] == 3 and
          most_common[1][1] == 1)

assert three_of_a_kind(['AH', 'AS', 'AD', 'TC', '2H'])
assert not three_of_a_kind(['AH', 'AS', 'AD', 'AC', '2H'])

def full_house(hand):
  most_common = Counter(hand_values(hand)).most_common()
  return (len(most_common) == 2 and
          most_common[0][1] == 3 and
          most_common[1][1] == 2)

assert full_house(['3S', '2S', '2C', '3D', '3H'])
assert not full_house(['3S', '2S', 'QC', '3D', '3H'])

def two_pairs(hand):
  most_common = Counter(hand_values(hand)).most_common()
  return (len(most_common) > 2 and
          most_common[0][1] == 2 and
          most_common[1][1] == 2)

assert two_pairs(['QS', 'QH', '3C', '3D', 'AS'])
assert not two_pairs(['QS', 'QH', '3C', '4D', 'AS'])
assert not two_pairs(['KS', 'QH', '3C', '3D', 'AS'])

def one_pair(hand):
  most_common = Counter(hand_values(hand)).most_common()
  return (len(most_common) > 2 and
          most_common[0][1] == 2 and
          most_common[1][1] == 1)

assert one_pair(['KS', 'KH', 'TC', '3H', '7H'])

# Lower numerical rank is better.
def rank(hand):
  hand_rank = [
    royal_flush,
    straight_flush,
    four_of_a_kind,
    full_house,
    flush,
    straight,
    three_of_a_kind,
    two_pairs,
    one_pair
  ]
  for i in xrange(len(hand_rank)):
    if hand_rank[i](hand):
      return i
  # high_card is last tested, defaults to true.  All hands have some high card.
  return len(hand_rank)

# Royal flush.
assert (rank(['AH', 'KH', 'QH', 'JH', 'TH']) == 0 and
        royal_flush(['AH', 'KH', 'QH', 'JH', 'TH']))
# Straight flush.
assert (rank(['4S', '3S', '2S', '5S', '6S']) == 1 and
        straight_flush(['4S', '3S', '2S', '5S', '6S']))
# Four of a kind.
assert (rank(['AH', 'AS', 'AD', 'AC', '2H']) == 2 and
        four_of_a_kind(['AH', 'AS', 'AD', 'AC', '2H']))
# Full house.
assert (rank(['3S', '2S', '2C', '3D', '3H']) == 3 and
        full_house(['3S', '2S', '2C', '3D', '3H']))
# Flush.
assert (rank(['2D', '3D', '4D', '5D', 'QD']) == 4 and
        flush(['2D', '3D', '4D', '5D', 'QD']))
# Straight.
assert (rank(['2D', '3D', '4D', '5D', '6C']) == 5 and
        straight(['2D', '3D', '4D', '5D', '6C']))
# Three of a kind.
assert (rank(['AH', 'AS', 'AD', 'TC', '2H']) == 6 and
        three_of_a_kind(['AH', 'AS', 'AD', 'TC', '2H']))
# Two pairs.
assert (rank(['QS', 'QH', '3C', '3D', 'AS']) == 7 and
        two_pairs(['QS', 'QH', '3C', '3D', 'AS']))
# One pair.
assert (rank(['KS', 'KH', 'TC', '3H', '7H']) == 8 and
        one_pair(['KS', 'KH', 'TC', '3H', '7H']))

# High card.
assert rank(['AS', '2C', 'QS', '3C', 'KS']) == 9

def game_winner(game):
  player1_hand = game[:5]
  player2_hand = game[(5 + 1):]

with open('poker.txt', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=' ')
  games = [row for row in reader]
