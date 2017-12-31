# Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

from collections import Counter

def primes(max_num):
  if max_num >= 2:
    prime_bitmap = [True for i in xrange(max_num)]
    prime_bitmap[0] = False
    prime_bitmap[1] = False
    for i in xrange(max_num):
      if prime_bitmap[i]:
        yield i
        for j in xrange(i ** 2, max_num, i):
          prime_bitmap[j] = False

def prime_factors(num):
  max_factor = int(num ** 0.5) + 1
  factors = Counter()
  for prime in primes(max_factor):
    while num % prime == 0:
      factors[prime] += 1
      num /= prime
    if num == 1:
      return factors
  if num > 1:
    factors[num] += 1
  return factors

def smallest_multiple(num):
  total_factors = Counter()
  for i in xrange(num + 1):
    total_factors |= prime_factors(i)
  result = 1
  for (prime, count) in total_factors.items():
    result *= prime ** count
  return result

print(smallest_multiple(20))
# 232792560
