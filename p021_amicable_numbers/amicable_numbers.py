# Amicable numbers
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
#
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
# and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
# and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

from collections import Counter
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

assert prime_factors(13 * 13).items() == [(13, 2)]

def divisors(num):
  factors = prime_factors(num)
  lst = [1]
  for prime, count in factors.items():
    lst = [elt * (prime ** i)
           for i in xrange(0, count + 1)
           for elt in lst]
  # lst[-1] == num, is not a proper divisor.
  return lst[:-1]

assert sum(divisors(220)) == 284

# Instead of building a list of divisors and then summing, compute sum_divisors
# directly, and use geometric_series_sum to save even more time.
def geometric_series_sum(r, n):
  return (r ** (n + 1) - 1) / (r - 1)

def sum_divisors(num):
  if num == 1:
    return 1
  factors = prime_factors(num)
  total = reduce(operator.mul,
                 (geometric_series_sum(prime, count)
                  for prime, count in factors.items()))
  # Subtract out num, which divides itself but is not a proper divisor.
  return total - num

def amicable_number(a):
  b = sum_divisors(a)
  return a != b and sum_divisors(b) == a

t0 = time.time()
result = sum(a for a in xrange(1, 10**4) if amicable_number(a))
t1 = time.time()

print(result)
print('time %f' % (t1 - t0))
# 31626
# time 0.335061

#-------------------------------------------------------------------------------
# Slower but much simpler code.
def sum_divisors_simple(num):
  return sum(i for i in xrange(1, num) if num % i == 0)

def amicable_number_simple(a):
  b = sum_divisors_simple(a)
  return a != b and sum_divisors_simple(b) == a

# t0 = time.time()
# result = sum(a for a in xrange(1, 10**4) if amicable_number_simple(a))
# t1 = time.time()
# print(result)
# print('time %f' % (t1 - t0))
# 31626
# time 3.969838

#-------------------------------------------------------------------------------
# Faster but less readable code.  Instead of storing prime factors in a
# Counter(), compute the sum immediately.
def sum_divisors_complex(num):
  if num == 1:
    return 0
  orig_num = num
  max_factor = int(num ** 0.5)
  prod = 1
  for prime in primes(max_factor + 1):
    count = 0
    while num % prime == 0:
      count += 1
      num /= prime
    if count > 0:
      prod *= geometric_series_sum(prime, count)
    if num == 1:
      # num is a divisor, but not a proper divisor, of num.
      return prod - orig_num
  if num != 1:
    # num itself is a prime factor.
    prod *= 1 + num
    # num is a divisor, but not a proper divisor, of num.
    return prod - orig_num

def amicable_number_complex(a):
  b = sum_divisors_complex(a)
  return a != b and sum_divisors_complex(b) == a

t0 = time.time()
result = sum(a for a in xrange(1, 10**4) if amicable_number_complex(a))
t1 = time.time()
print(result)
print('time %f' % (t1 - t0))
# 31627
# time 0.277421
# It's not much faser than the previous readable version.
