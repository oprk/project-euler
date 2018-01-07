# Pandigital prime
# Problem 41

# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
# also prime.

# What is the largest n-digit pandigital prime that exists?

import copy
import operator
import time

def primes(max_num):
  if max_num >= 2:
    prime_bitmap = [True for i in xrange(max_num)]
    prime_bitmap[0] = False
    prime_bitmap[1] = False
    for i in xrange(max_num):
      if prime_bitmap[i]:
        yield i
        for j in xrange(i**2, max_num, i):
          prime_bitmap[j] = False

# Largest pandigital is 987654321.  However, sum(xrange(10)) = 45, which is
# divisible by 3 and therefore not prime.
# sum(xrange(9)) = 36, which is also not prime.
# So largest pandigital is no greater than 7654321.
prime_lst = list(primes(int(7654321 ** 0.5) + 1))
prime_set = set(prime_lst)

def is_prime(n):
  if n < 2:
    return False
  max_num = int(n ** 0.5) + 1
  for p in prime_lst:
    if p >= max_num:
      break
    if n % p == 0:
      return False
  return True

# Starting from largest pandigital and working backwards.
def permutation(collection):
  if not collection:
    yield collection
  else:
    for i in xrange(len(collection)):
      elt = collection[i]
      new_collection = collection[:i] + collection[(i + 1):]
      for perm in permutation(new_collection):
        yield [elt] + perm

def int_digits_to_int(int_lst):
  n = 0
  for elt in int_lst:
    n *= 10
    n += elt
  return n

def largest_pandigital_prime():
  # Starting from largest 7 digit pandigital:
  for digits in xrange(7, 0, -1):
    for perm in permutation(list(xrange(digits, 0, -1))):
      candidate = int_digits_to_int(perm)
      if is_prime(candidate):
        return candidate

t0 = time.time()
result = largest_pandigital_prime()
t1 = time.time()
print(result)
print('time %f' % (t1 - t0))
# 7652413
# time 0.000157
