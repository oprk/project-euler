# Longest Collatz sequence
#
# The following iterative sequence is defined for the set of positive integers:
#   n -> n / 2 (n is even)
#   n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#   13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

import time

memo = {1 : 1}

def collatz_length(num):
  if num not in memo:
    if num % 2 == 0:
      memo[num] = collatz_length(num / 2) + 1
    else:
      memo[num] = collatz_length(3 * num + 1) + 1
  return memo[num]

t0 = time.time()
best_length = 1
best_number = 1
for i in xrange(1, 10**6):
  length = collatz_length(i)
  if best_length < length:
    best_length = length
    best_number = i
t1 = time.time()
  
print(best_number)
print('time %f' % (t1 - t0))
# 837799
# time 1.468122
