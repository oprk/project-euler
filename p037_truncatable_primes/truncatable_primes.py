# Truncatable primes

# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime at
# each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
# 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to
# right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import time

class Prime:
  def __init__(self):
    self.max_num = 0
    self.prime_bitmap = []
    self.prime_lst = []

  def mark_prime(self, max_num):
    # Double each time max_num is exceeded.
    if max_num > self.max_num:
      new_max_num = max(2, max(max_num, 2 * self.max_num))
      self.prime_bitmap += [True for i in xrange(self.max_num, new_max_num)]
      self.max_num = new_max_num
      self.prime_bitmap[0] = False
      self.prime_bitmap[1] = False
      for i in xrange(self.max_num):
        if self.prime_bitmap[i]:
          self.prime_lst.append(i)
          for j in xrange(i**2, self.max_num, i):
            self.prime_bitmap[j] = False

primes = Prime()

# s is str(integer).
def truncate_left(s):
  return s[1:]

# s is str(integer).
def truncate_right(s):
  return s[:-1]

# Look at all the truncatable primes we've generated so far, and observe that
# adding a 1, 3, 7 or 9 would not make it prime; then we know we have to stop.
# How many truncatable from left primes can we make before we have to stop?

# Save time on primality test by only computing primes up to square root.
def is_prime(num):
  if num < 2:
    return False
  max_num = int(num ** 0.5) + 1
  primes.mark_prime(max_num)
  for p in primes.prime_lst:
    if p >= max_num:
      break
    if num % p == 0:
      return False
  return True

# s is str(integer).
def truncatable_prime(s, truncate_direction, memo):
  if not s:
    return True
  else:
    if s not in memo:
      memo[s] = (is_prime(int(s)) and
                 truncatable_prime(truncate_direction(s),
                                   truncate_direction, memo))
    return memo[s]

memo_left = {}
def truncatable_prime_from_left(s):
  return truncatable_prime(s, truncate_left, memo_left)

memo_right = {}
def truncatable_prime_from_right(s):
  return truncatable_prime(s, truncate_right, memo_right)


t0 = time.time()

d = 1
truncatable_from_right = {1 : ['2', '3', '5', '7']}
while truncatable_from_right[d]:
  d += 1
  truncatable_from_right[d] = []
  for t in truncatable_from_right[d - 1]:
    for p in ['1', '3', '7', '9']:
      if truncatable_prime_from_right(t + p):
        truncatable_from_right[d].append(t + p)

total = 0
for d in truncatable_from_right:
  # Single digit primes are not truncatable.
  if d == 1:
    continue
  for p in truncatable_from_right[d]:
    if truncatable_prime_from_left(p):
      total += int(p)

t1 = time.time()


print(total)
print('time %f' % (t1 - t0))
# 748317
# time 0.024879
