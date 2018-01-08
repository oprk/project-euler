# Combinatoric selections
# Problem 53
# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 5C3 = 10.

# In general,

# nCr =	n! / (r!(n−r)!)
# where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

# How many, not necessarily distinct, values of nCr, for 1 ≤ n ≤ 100, are
# greater than one-million?

import operator
import time

def n_choose_r(n, r):
  return (reduce(operator.mul, xrange(n - r + 1, n + 1)) /
          reduce(operator.mul, xrange(1, r + 1)))

assert n_choose_r(5, 3) == 10

t0 = time.time()
count = 0
for n in xrange(1, 100 + 1):
  for r in xrange(1, n):
    if n_choose_r(n, r) > 1000000:
      count += 1
t1 = time.time()
print(count)
print('time %f' % (t1 - t0))
# 4075
# time 0.035131
