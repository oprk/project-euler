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

from collections import Counter

class Primes:
  def __init__(self):
    self.max_num = 1
    self.prime_bitmap = [False for i in xrange(2)]
    self.prime_lst = []

  def mark_prime(self, n):
    new_max_num = max(n, self.max_num * 2)
    self.prime_bitmap += [True for i in xrange(self.max_num, new_max_num + 1)]
    self.prime_lst = []
    for i in xrange(new_max_num + 1):
      if self.prime_bitmap[i]:
        self.prime_lst.append(i)
        for j in xrange(i**2, new_max_num + 1, i):
          self.prime_bitmap[j] = False

  def is_prime(self, n):
    self.mark_prime(n)
    return self.prime_bitmap[n]

  def prime_factors(self, n):
    max_num = int(n ** 0.5) + 1
    self.mark_prime(max_num)
    factors = Counter()
    for prime in self.prime_lst:
      while n % prime == 0:
        factors[prime] += 1
        n /= prime
      if n == 1:
        return factors
    if n != 1:
      # n itself is prime.
      factors[n] += 1
    return factors

p = Primes()

a = 1
b = 2
c = 3
num_factors_a = len(p.prime_factors(a))
num_factors_b = len(p.prime_factors(b))
num_factors_c = len(p.prime_factors(c))

while True:
  d = c + 1
  num_factors_d = len(p.prime_factors(d))
  if num_factors_a == num_factors_b == num_factors_c == num_factors_d == 4:
    break
  a = b
  b = c
  c = d
  num_factors_a = num_factors_b
  num_factors_b = num_factors_c
  num_factors_c = num_factors_d

print(a)
