# Non-abundant sums.

# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of 28
# would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers is
# less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

from collections import Counter
import operator
import time

def sum_divisors_simple(num):
  return sum(i for i in xrange(1, num) if num % i == 0)

assert sum_divisors_simple(1) == 0
assert sum_divisors_simple(12) == 16

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

def prime_factors(num):
  max_factor = int(num ** 0.5)
  factors = Counter()
  for prime in primes(max_factor + 1):
    while num % prime == 0:
      factors[prime] += 1
      num /= prime
    if num == 1:
      return factors
  if num != 1:
    # num itself is a prime factor.
    factors[num] += 1
    return factors

assert prime_factors(13 ** 2).items() == [(13, 2)]

def geometric_series_sum(r, n):
  return (r ** (n + 1) - 1) / (r - 1)

def sum_divisors(num):
  if num <= 1:
    # 1 does not have any prime factors.
    return 0
  return reduce(operator.mul,
                (geometric_series_sum(prime, count)
                 for prime, count in prime_factors(num).items())) - num

assert sum_divisors(1) == 0
assert sum_divisors(12) == 16

# Speed things up by caching and only checking abundant numbers.
t0 = time.time()

max_num = 28123
abundant_numbers = [i for i in xrange(max_num) if sum_divisors(i) > i]
abundant_set = set(abundant_numbers)

def abundant_sum_v2(n):
  max_a = n / 2 + 1
  for a in abundant_numbers:
    if a > max_a:
      break
    b = n - a
    if b in abundant_set:
      return True
  return False

result = sum(i for i in xrange(1, max_num + 1) if not abundant_sum_v2(i))

t1 = time.time()
print result
print('time %f' % (t1 - t0))
# 4179871
# time 0.988464
