# Champernowne's constant
# Problem 40
# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...
#  .-----------^ 12
#  .--------------------------------^ 33
#
# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

# 1-9, 9 1-digits
# 10-99, 90 2-digits
# 100-999, 900 3-digits

import operator
import time

def champernownes_constant_nth_digit(n):
  # nth digit is 1-indexed.
  n -= 1
  num_digits = 1
  num = 9 * 10 ** (num_digits - 1)
  while n > num:
    n -= num * num_digits
    num_digits += 1
    num *= 10
  div = n / num_digits
  rem = n % num_digits
  return int(str(10**(num_digits - 1) + div)[rem])

t0 = time.time()
result = reduce(operator.mul,
                (champernownes_constant_nth_digit(10**i)
                 for i in xrange(7)))
t1 = time.time()
print(result)
print('time %f' % (t1 - t0))
# 210
# time 0.000039
