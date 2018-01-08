# Distinct primes factors
# Problem 47
# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors
# each. What is the first of these numbers?

import time

t0 = time.time()
# Search under 1 million for now.
max_num = 1000000
# Number of prime factors.
factors = [0] * max_num
count = 0
for i in xrange(2, max_num):
  if factors[i] == 0:
    # i is prime
    count = 0
    for j in xrange(i, max_num, i):
      factors[j] += 1
  elif factors[i] == 4:
    count += 1
    if count == 4:
      print i - 3 # First number
      break
  else:
    count = 0
t1 = time.time()
print('time %f' % (t1 - t0))
# 134043
# time 0.345344
