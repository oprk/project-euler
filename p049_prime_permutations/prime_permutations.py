# Prime permutations
# Problem 49

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms are
# prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this
# sequence?

from collections import defaultdict
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

t0 = time.time()

prime_lst = list(primes(10**5))

primes_by_sorted_digits = defaultdict(list)
for prime in prime_lst:
  if prime >= 1000 and prime < 10000:
    primes_by_sorted_digits[''.join(sorted(str(prime)))].append(prime)

for k in primes_by_sorted_digits:
  v = sorted(primes_by_sorted_digits[k])
  n = len(v)
  if n >= 3:
    for i in xrange(n):
      for j in xrange(i + 1, n):
        if (2 * v[j] - v[i]) in v:
          print ''.join(str(i) for i in [v[i], v[j], (2 * v[j] - v[i])])

t1 = time.time()
print('time %f' % (t1 - t0))
# 296962999629
# 148748178147
# time 0.023019
