# Coin sums
#
# In England the currency is made up of pound, £, and pence, p, and there are
# eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

import time

coins = [1, 2, 5, 10, 20, 50, 100, 200]

memo = {}

def make_change(coins, amount):
  if amount < 0 or not coins:
    return 0
  if amount == 0:
    return 1
  min_coin = coins[0]
  if (min_coin, amount) not in memo:
    memo[(min_coin, amount)] = (make_change(coins, amount - min_coin) +
                                make_change(coins[1:], amount))
  return memo[(min_coin, amount)]

t0 = time.time()
result = make_change(coins, 200)
t1 = time.time()

print(result)
print('time %f' % (t1 - t0))
# 73682
# time 0.001619
