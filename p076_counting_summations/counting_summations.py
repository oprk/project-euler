"""
Counting summations

Problem 76
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

"""
This is like making change, except we can make change with xrange(1, target) coins.
"""

memo = {}

def make_change(max_coin, amount):
  if amount < 0 or max_coin < 1:
    return 0
  if amount == 0:
    return 1
  if (max_coin, amount) not in memo:
    # We either use the max coin, or skip it.
    memo[(max_coin, amount)] = (make_change(max_coin, amount - max_coin) +
                                make_change(max_coin - 1, amount))
  return memo[(max_coin, amount)]


"""
>>> make_change(4, 5)
make_change(4, 5)
6
>>> make_change(99, 100)
make_change(99, 100)
190569291
"""
