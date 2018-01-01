# Lexicographic permutations
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?

import time

# there are 9! permutations that start with 0
# there are 9! permutations that start with 1
# ...

def fact(n):
  if n <= 1:
    return 1
  else:
    return fact(n - 1) * n

def lexicographic_permutations(num_digits, n):
  assert n < fact(num_digits)
  digits = [str(i) for i in xrange(num_digits)]
  perm = []
  for i in xrange(num_digits - 1, 0 - 1, -1):
    p = fact(i)
    digit = digits[n / p]
    perm.append(digit)
    digits.remove(digit)
    n %= p
  return perm

t0 = time.time()
result = int(''.join(lexicographic_permutations(10, 10**6 - 1)))
t1 = time.time()

print(result)
print('time %f' % (t1 - t0))
# 2783915460
# time 0.000029
