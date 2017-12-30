# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?

# Implement prime sieve.

import math

def primes(max_num):
  prime_bitmap = [True for x in xrange(max_num)]
  prime_bitmap[0] = False
  prime_bitmap[1] = False
  for i in xrange(max_num):
    if prime_bitmap[i]:
      yield i
      for j in xrange(i**2, max_num, i):
        prime_bitmap[j] = False

def smallest_prime_factor(num):
  max_factor = int(num ** 0.5) + 1
  for prime in primes(max_factor + 1):
    if num % prime == 0:
      return prime
  # num itself is prime (or 1).
  return num

def prime_factors(num):
  while num > 1:
    prime_factor = smallest_prime_factor(num)
    num /= prime_factor
    yield prime_factor

max(prime_factors(600851475143))

