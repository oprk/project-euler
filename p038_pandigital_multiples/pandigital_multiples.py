# Pandigital multiples
# Problem 38
# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
# call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
# 5, giving the pandigital, 918273645, which is the concatenated product of 9
# and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1,2, ... , n) where n > 1?

import time

def pandigital_multiple(num):
  pandigital = str(num)
  # i > 1
  for i in xrange(2, 10):
    pandigital += str(num * i)
    if len(set(pandigital)) != len(pandigital):
      # Not a pandigital because we are repeating digits.
      return None
    elif len(pandigital) == 9:
        return pandigital

# Largest multiple without overflowing 9 digits is 9999

t0 = time.time()

best = 0
for i in xrange(10000):
  s = pandigital_multiple(i)
  if s is not None:
    best = max(int(s), best)

t1 = time.time()

print(best)
print('time %f' % (t1 - t0))
# 935218704
# time 0.017419


# To make the largest pandigital number, we probably want the most significant
# digit to be 9.
t0 = time.time()
best = 0
for i in xrange(1000):
  s = pandigital_multiple(int('9' + str(i)))
  if s is not None:
    best = max(int(s), best)
t1 = time.time()

print(best)
print('time %f' % (t1 - t0))
# 935218704
# time 0.002172
