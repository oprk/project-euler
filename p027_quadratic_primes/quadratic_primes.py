# Quadratic primes
#
# Euler discovered the remarkable quadratic formula:
#   n^2 + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive
# integer values 0 <= n <= 39.
#
# However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and
# certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
#
# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80
# primes for the consecutive values 0 <= n <= 79.  The product of the
# coefficients, -79 and 1601, is -126479.
#
# Consider quadratics of the form:
#   n^2 + an + b, where |a| < 1000 and |b| <= 1000
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11, |-4| = 4
#
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n=0.

import time

class QuadraticPrimes:
  def __init__(self, max_num):
    self.max_num = max(2, max_num)
    self.prime_bitmap = [True for i in xrange(self.max_num + 1)]
    self.prime_bitmap[0] = False
    self.prime_bitmap[1] = False
    self.mark_prime(2, self.max_num)

  def mark_prime(self, start_num, max_num):
    for i in xrange(start_num, max_num + 1):
      if self.prime_bitmap[i]:
        for j in xrange(i**2, max_num + 1, i):
          self.prime_bitmap[j] = False

  def is_prime(self, num):
    if num <= 0:
      return False
    if num >= self.max_num:
      # Extend prime_bitmap.
      new_max_num = max(num, 2 * self.max_num)
      self.prime_bitmap += [True for i in xrange(self.max_num, new_max_num + 1)]
      self.mark_prime(2, new_max_num)
      self.max_num = new_max_num
    return self.prime_bitmap[num]

  def consecutive_primes(self, a, b):
    n = 0
    while True:
      p = n**2 + (a * n) + b
      if self.is_prime(p):
        n += 1
      else:
        return n

t0 = time.time()

# Make prime set for b <= 1000.
qp = QuadraticPrimes(1000)
prime_set_1000 = set(i for i in xrange(qp.max_num + 1) if qp.prime_bitmap[i])

best_ab = None
best_len = 0
# a has to be odd, otherwise when n is odd, n^2 + an + b is even.
for a in xrange(-1000 + 1, 1000, 2):
  # Consider when n = 0.  b has to be prime.
  for b in prime_set_1000:
    k = qp.consecutive_primes(a, b)
    if best_len < k:
      best_len = k
      best_ab = (a, b)

t1 = time.time()

print('longest sequence: %d' % best_len)
print('a = %d, b = %d' % best_ab)
print(best_ab[0] * best_ab[1])
print('time %f' % (t1 - t0))
# longest sequence: 71
# a = -61, b = 971
# -59231
# time 0.179464
