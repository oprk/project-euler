# Digit fifth powers
#
# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
#
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers
# of their digits.

import time

def digit_powers(pow, num):
  return sum(int(c)**pow for c in str(num))

assert digit_powers(4, 1634) == 1634
assert digit_powers(4, 8208) == 8208

# When to stop searching?
# When maximum digit sum 9**5 * num_digits < 10**num_digits

# num_digits = 1
# while ((9 ** 5) * num_digits) > (10 ** (num_digits - 1)):
#   print('%d > %d' % (((9 ** 5) * num_digits), (10 ** (num_digits - 1))))
#   num_digits += 1
# print('%d < %d' % (((9 ** 5) * num_digits), (10 ** (num_digits - 1))))
# print(num_digits)
# 59049 > 1
# 118098 > 10
# 177147 > 100
# 236196 > 1000
# 295245 > 10000
# 354294 > 100000
# 413343 < 1000000
# 7


t0 = time.time()
result = sum(i for i in xrange(2, 9 ** 5 * 6) if digit_powers(5, i) == i)
t1 = time.time()
print(result)
print('time %f' % (t1 - t0))
# 443839
# time 1.268354

# for i in xrange(2, 9 ** 5 * 6):
#   if digit_powers(5, i) == i:
#     print(i)
# 4150
# 4151
# 54748
# 92727
# 93084
# 194979

# Another approach is to consider the possible sets of 6 digits.
# 000000 to 012345 to 999999 (notice the digits are sorted).
# At each digit, we can emit the same digit, or go up in value (multiple times).

def digit_sets(min_value, num_digits):
  if num_digits > 0:
    for i in xrange(min_value, 9 + 1):
      for elt in digit_sets(i, num_digits - 1):
        yield [i] + elt
  else:
    yield []

t0 = time.time()

max_num_digits = 6
for digit_set in digit_sets(0, max_num_digits):
  power_sum = sum(x**5 for x in digit_set)
  power_sum_digits = [int(c) for c in sorted(str(power_sum))]
  # Pad with the correct number of zeros.
  power_sum_digits = ([0 for i in xrange(max_num_digits - len(power_sum_digits))] +
                      power_sum_digits)
  if power_sum_digits == digit_set:
    print(power_sum)

t1 = time.time()

print('time %f' % (t1 - t0))
# time 0.039229
