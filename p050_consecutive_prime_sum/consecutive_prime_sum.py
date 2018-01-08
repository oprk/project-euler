# Consecutive prime sum
# Problem 50
# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import time

def primes_sums(max_num):
  if max_num >= 2:
    prime_bitmap = [True for i in xrange(max_num)]
    prime_bitmap[0] = False
    prime_bitmap[1] = False
    running_sum = 0
    yield (0, 0)
    for i in xrange(max_num):
      if prime_bitmap[i]:
        running_sum += i
        yield (i, running_sum)
        for j in xrange(i**2, max_num, i):
          prime_bitmap[j] = False

t0 = time.time()
primes_sums_lst = list(primes_sums(10**6))
primes_set = set(k for (k, v) in primes_sums_lst)

n = len(primes_sums_lst)
best_n = 0
best_prime = 0
for i in xrange(n):
  for j in xrange(i + 21, n):
    consecutive_sum = primes_sums_lst[j][1] - primes_sums_lst[i][1]
    if consecutive_sum >= 1000000:
      break
    if consecutive_sum in primes_set:
      num_primes = primes_sums_lst[j][0] - primes_sums_lst[i][0]
      if best_n < num_primes:
        best_n = num_primes
        best_prime = consecutive_sum

t1 = time.time()
print(best_prime)
print('time %f' % (t1 - t0))
# 997651
# time 0.413729
