# Circular primes
#
# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.
#
# How many circular primes are there below one million?

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

def int_to_digits(n):
  lst = []
  while n > 0:
    lst.append(n % 10)
    n /= 10
  return list(reversed(lst))

def digits_to_int(digits):
  n = 0
  for d in digits:
    n = (n * 10) + d
  return n

def rotate(digits, i):
  return digits[i:] + digits[:i]

prime_set = set(prime for prime in primes(10**6))

t0 = time.time()
# 2 and 5 are circular primes.
total = 2
for prime in prime_set:
  # Primes that contain even numbers won't be prime when rotated.
  # Primes that contain 5 won't be prime when rotated.
  digits = int_to_digits(prime)
  if (all(digit in (1, 3, 7, 9) for digit in digits) and
      all(digits_to_int(rotate(digits, rot)) in prime_set
          for rot in xrange(1, len(digits)))):
    total += 1
t1 = time.time()

print(total)
print('time %f' % (t1 - t0))
# 55
# 0.216004
