# Spiral primes
# Problem 58

# Starting with 1 and spiralling anticlockwise in the following way, a square
# spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right
# diagonal, but what is more interesting is that 8 out of the 13 numbers lying
# along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

# If one complete new layer is wrapped around the spiral above, a square spiral
# with side length 9 will be formed. If this process is continued, what is the
# side length of the square spiral for which the ratio of primes along both
# diagonals first falls below 10%?

import time

def spiral():
  l = 2
  i = 1
  while True:
    for _ in xrange(4):
      i += l
      yield i
    l += 2

class Prime:

  def __init__(self):
    self.max_num = 0
    self.prime_bitmap = []
    self.prime_set = set([])
    self.prime_lst = []

  def mark_prime(self, max_num):
    if max_num > self.max_num:
      new_max_num = max(max_num, self.max_num * 2)
      self.prime_lst = []
      self.prime_bitmap = [True for _ in xrange(new_max_num + 1)]
      self.prime_bitmap[0] = False
      self.prime_bitmap[1] = False
      for i in xrange(new_max_num + 1):
        if self.prime_bitmap[i]:
          self.prime_lst.append(i)
          self.prime_set.add(i)
          for j in xrange(i**2, new_max_num + 1, i):
            self.prime_bitmap[j] = False
      self.max_num = new_max_num

  def is_prime(self, n):
    if n <= self.max_num:
      return n in self.prime_set
    else:
      max_num = int(n**0.5) + 1
      self.mark_prime(max_num)
      for p in self.prime_lst:
        if p > max_num:
          return True
        if n % p == 0:
          return False
      return True

def spiral_primes():
  p = Prime()
  count = 1
  prime_count = 0
  for elt in spiral():
    count += 1
    if p.is_prime(elt):
      prime_count += 1
    if (count % 4) == 1:
      # Check the ratio.
      if prime_count < (count * 0.1):
        return int(elt ** 0.5)

t0 = time.time()
result = spiral_primes()
t1 = time.time()
print(result)
print('time %f' % (t1 - t0))
# 26241
# time 0.934496
