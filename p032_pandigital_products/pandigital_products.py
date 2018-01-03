# Pandigital products
#
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.

# Each digit of 123456789 can be labeled as in group a, b or c, where a x b = c.
# Regardless of whether the expression formed makes any sense, there are
# 3**9 / 2 = 9841.5 unique set(set(a), set(b))
# Each set of digits for a and b each have their own permutations as well.

import time

t0 = time.time()
products = 0
for a in range(4, 99):
  if a % 10 and a % 11:
    for b in range(123, 10000 / a):
      c = a * b
      nums = set(list(str(a) + str(b) + str(c)))
      if len(nums) == 9 and not '0' in nums:
        products += c
t1 = time.time()
print(products)
print('time %f' % (t1 - t0))
# 45228
# time 0.028677
