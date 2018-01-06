# Truncatable primes

# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime at
# each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
# 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to
# right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

# def primes(max_num):
#   if max_num >= 2:
#     prime_bitmap = [True for i in xrange(max_num)]
#     prime_bitmap[0] = False
#     prime_bitmap[1] = False
#     for i in xrange(max_num):
#       if prime_bitmap[i]:
#         yield i
#         for j in xrange(i**2, max_num, i):
#           prime_bitmap[j] = False

class Prime:
  def __init__(self):
    self.max_num = 0
    self.prime_bitmap = []
    self.prime_set = set([])

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
          self.prime_set.add(i)
          for j in xrange(i**2, self.max_num, i):
            self.prime_bitmap[j] = False

  def is_prime(self, num):
    self.mark_prime(num + 1)
    return num in self.prime_set

primes = Prime()

# s is str(integer).
def truncate_left(s):
  return s[1:]

# s is str(integer).
def truncate_right(s):
  return s[:-1]

# s is str(integer).
def truncatable_prime(s, truncate_direction, memo):
  if not s:
    return True
  else:
    if s not in memo:
      memo[s] = (primes.is_prime(int(s)) and
                 truncatable_prime(truncate_direction(s),
                                   truncate_direction, memo))
    return memo[s]

memo_left = {}
def truncatable_prime_from_left(s):
  return truncatable_prime(s, truncate_left, memo_left)

memo_right = {}
def truncatable_prime_from_right(s):
  return truncatable_prime(s, truncate_right, memo_right)

primes.mark_prime(1000000)

for p in primes.prime_set:
  if truncatable_prime_from_left(str(p)) and truncatable_prime_from_right(str(p)):
    print(p)

# [k for k in memo_left if memo_left[k]]

# Look at all the truncatable primes we've generated so far, and observe that
# adding a 1, 3, 7 or 9 would not make it prime; then we know we have to stop.
# How many truncatable from left primes can we make before we have to stop?
