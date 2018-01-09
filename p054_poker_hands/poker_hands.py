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
# suites = ['H', 'S', 'D', 'C']

class Poker:
  high_card = 0
  one_pair = 1
  two_pairs = 2
  three_of_a_kind = 3
  straight = 4
  flush = 5
  full_house = 6
  four_of_a_kind = 7
  straight_flush = 8
  royal_flush = 9

  values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
  }


def hand_suites(hand):
  return [card[1] for card in hand]

def hand_values(hand):
  return [card[0] for card in hand]

def ordered_hand_value_ranks(hand):
  return list(reversed(sorted(Poker.values[value] for value in hand_values(hand))))

def flush(hand):
  if len(set(hand_suites(hand))) != 1:
    return None
  else:
    return (Poker.flush, ordered_hand_value_ranks(hand))

assert flush(['2D', '3D', '4D', '5D', '6D']) == (Poker.flush, [6, 5, 4, 3, 2])
assert flush(['2H', '3D', '4D', '5D', '6D']) is None

def royal_flush(hand):
  if flush(hand) and set(hand_values(hand)) == set(['T', 'J', 'Q', 'K', 'A']):
    return (Poker.royal_flush, ordered_hand_value_ranks(hand))
  return None

assert royal_flush(['AH', 'KH', 'QH', 'JH', 'TH']) == (Poker.royal_flush, [14, 13, 12, 11, 10])
assert royal_flush(['AH', 'KS', 'QH', 'JH', 'TH']) is None
assert royal_flush(['AH', '2H', 'QH', 'JH', 'TH']) is None

def straight(hand):
  order = ordered_hand_value_ranks(hand)
  curr = order[0]
  rest = order[1:]
  for elt in rest:
    if curr - elt != 1:
      return None
    curr = elt
  return (Poker.straight, order)

assert straight(['4S', '3H', '2H', '5D', '6C']) == (Poker.straight, [6, 5, 4, 3, 2])
assert straight(['4S', '3H', '2H', 'TD', '6C']) is None

def straight_flush(hand):
  return straight(hand) and flush(hand)

assert straight_flush(['4S', '3S', '2S', '5S', '6S'])
assert not straight_flush(['4S', '3H', '2H', '5D', '6C'])

def four_of_a_kind(hand):
  most_common = Counter(hand_values(hand)).most_common()
  if most_common[0][1] == 4:
    four = [Poker.values[most_common[0][0]]] * 4
    single = [Poker.values[most_common[1][0]]]
    return (Poker.four_of_a_kind, four + single)
  return None

assert (four_of_a_kind(['AH', 'AS', 'AD', 'AC', '2H']) ==
        (Poker.four_of_a_kind, [14, 14, 14, 14, 2]))
assert four_of_a_kind(['AH', 'AS', 'AD', 'TC', '2H']) is None

def three_of_a_kind(hand):
  most_common = Counter(hand_values(hand)).most_common()
  if (len(most_common) > 2 and
      most_common[0][1] == 3 and
      most_common[1][1] == 1):
    three = [Poker.values[most_common[0][0]]] * 3
    singles = list(reversed(sorted(
      [Poker.values[most_common[i][0]] for i in xrange(1, 3)])))
    return (Poker.three_of_a_kind, three + singles)
  return None

assert (three_of_a_kind(['AH', 'AS', 'AD', 'TC', '2H']) ==
        (Poker.three_of_a_kind, [14, 14, 14, 10, 2]))
assert three_of_a_kind(['AH', 'AS', 'AD', 'AC', '2H']) is None

def full_house(hand):
  most_common = Counter(hand_values(hand)).most_common()
  if (len(most_common) == 2 and
      most_common[0][1] == 3 and
      most_common[1][1] == 2):
    three = [Poker.values[most_common[0][0]]] * 3
    pair = [Poker.values[most_common[1][0]]] * 2
    return (Poker.full_house, three + pair)
  return None

assert (full_house(['2S', '3S', '3C', '2D', '2H']) ==
        (Poker.full_house, [2, 2, 2, 3, 3]))
assert full_house(['3S', '2S', 'QC', '3D', '3H']) is None

def two_pairs(hand):
  most_common = Counter(hand_values(hand)).most_common()
  if (len(most_common) > 2 and
      most_common[0][1] == 2 and
      most_common[1][1] == 2):
    pairs = list(reversed(sorted(
      ([Poker.values[most_common[0][0]]] * 2) +
      ([Poker.values[most_common[1][0]]] * 2))))
    single = [Poker.values[most_common[2][0]]]
    return (Poker.two_pairs, pairs + single)
  return None

assert (two_pairs(['QS', 'QH', '3C', '3D', 'AS']) ==
        (Poker.two_pairs, [12, 12, 3, 3, 14]))
assert two_pairs(['QS', 'QH', '3C', '4D', 'AS']) is None
assert two_pairs(['KS', 'QH', '3C', '3D', 'AS']) is None

def one_pair(hand):
  most_common = Counter(hand_values(hand)).most_common()
  if (len(most_common) > 2 and
      most_common[0][1] == 2 and
      most_common[1][1] == 1):
    pair = [Poker.values[most_common[0][0]]] * 2
    singles = list(reversed(sorted(
      [Poker.values[most_common[i][0]] for i in xrange(1, 4)])))
    return (Poker.one_pair, pair + singles)
  return None

assert (one_pair(['KS', 'KH', 'TC', '3H', '7H']) ==
        (Poker.one_pair, [13, 13, 10, 7, 3]))

def high_card(hand):
  most_common = Counter(hand_values(hand)).most_common()
  if (len(most_common) == 5 and
      straight(hand) is None and
      flush(hand) is None):
    return (Poker.high_card, ordered_hand_value_ranks(hand))
  return None

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
    one_pair,
    high_card
  ]
  for f in hand_rank:
    result = f(hand)
    if result is not None:
      return result
  # This case should be impossible.
  assert False

# Royal flush.
assert (rank(['AH', 'KH', 'QH', 'JH', 'TH']) ==
        royal_flush(['AH', 'KH', 'QH', 'JH', 'TH']))
# Straight flush.
assert (rank(['4S', '3S', '2S', '5S', '6S']) ==
        straight_flush(['4S', '3S', '2S', '5S', '6S']))
# Four of a kind.
assert (rank(['AH', 'AS', 'AD', 'AC', '2H']) ==
        four_of_a_kind(['AH', 'AS', 'AD', 'AC', '2H']))
# Full house.
assert (rank(['3S', '2S', '2C', '3D', '3H']) ==
        full_house(['3S', '2S', '2C', '3D', '3H']))
# Flush.
assert (rank(['2D', '3D', '4D', '5D', 'QD']) ==
        flush(['2D', '3D', '4D', '5D', 'QD']))
# Straight.
assert (rank(['2D', '3D', '4D', '5D', '6C']) ==
        straight(['2D', '3D', '4D', '5D', '6C']))
# Three of a kind.
assert (rank(['AH', 'AS', 'AD', 'TC', '2H']) ==
        three_of_a_kind(['AH', 'AS', 'AD', 'TC', '2H']))
# Two pairs.
assert (rank(['QS', 'QH', '3C', '3D', 'AS']) ==
        two_pairs(['QS', 'QH', '3C', '3D', 'AS']))
# One pair.
assert (rank(['KS', 'KH', 'TC', '3H', '7H']) ==
        one_pair(['KS', 'KH', 'TC', '3H', '7H']))
# High card.
assert (rank(['AS', '2C', 'QS', '3C', 'KS']) ==
        high_card(['AS', '2C', 'QS', '3C', 'KS']))

def sorted_hand_values(hand):
  return list(reversed(sorted(Poker.values[c] for c in hand_values(hand))))

def player1_wins(game):
  player1_hand = game[:5]
  player2_hand = game[5:]
  return rank(player1_hand) > rank(player2_hand)


with open('poker.txt', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=' ')
  games = [row for row in reader]
  result = sum(player1_wins(game) for game in games)

print(result)
# 376
