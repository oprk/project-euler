# Goldbach's other conjecture
# Problem 46

# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.

# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a
# prime and twice a square?

import time

def square(n):
  return int(n ** 0.5)**2 == n

class Primes:
  def __init__(self):
    self.max_num = 1
    self.prime_bitmap = [False for i in xrange(2)]
    self.prime_lst = []

  def mark_prime(self, n):
    if n > self.max_num:
      new_max_num = max(n, self.max_num * 2)
      self.prime_bitmap += [True for i in xrange(new_max_num + 1)]
      self.prime_lst = []
      for i in xrange(new_max_num + 1):
        if self.prime_bitmap[i]:
          self.prime_lst.append(i)
          for j in xrange(i**2, new_max_num + 1, i):
            self.prime_bitmap[j] = False
      self.max_num = new_max_num

  def is_prime(self, n):
    self.mark_prime(n)
    return self.prime_bitmap[n]

def composite_sum_of_prime_and_twice_square(i, p):
  assert not p.is_prime(i)
  for prime in p.prime_lst:
    if prime > i:
      return False
    if square((i - prime) / 2):
      return True

def goldbach():
  p = Primes()
  i = 9
  while True:
    if not p.is_prime(i) and not composite_sum_of_prime_and_twice_square(i, p):
        return i
    i += 1

t0 = time.time()
result = goldbach()
t1 = time.time()
print(result)
print('time %f' % (t1 - t0))
# 5777
# time 0.122437
