# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?

# Implement prime sieve.

def primes(max_num):
  prime_bitmap = [True for x in xrange(max_num)]
  prime_bitmap[0] = False
  prime_bitmap[1] = False
  for i in xrange(max_num):
    if prime_bitmap[i]:
      yield i
      for j in xrange(i**2, max_num, i):
        prime_bitmap[j] = False

def prime_factors(num):
  max_factor = int(num**0.5)
  for prime in primes(max_factor):
    if num % prime == 0:
      yield prime

list(prime_factors(600851475143))[-1]
# 6857
