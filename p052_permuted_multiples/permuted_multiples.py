# Permuted multiples
# Problem 52

# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.

import time

def permuted_multiples(i):
  digits = list(sorted(str(i)))
  j = 2
  while digits == list(sorted(str(j * i))):
    j += 1
  return j - 1

t0 = time.time()
i = 1
while permuted_multiples(i) < 6:
  i += 1
t1 = time.time()
print(i)
print('time %f' % (t1 - t0))
# 142857
# time 0.384030
