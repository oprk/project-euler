# Multiples of 3 and 5
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_of_3_and_5(max_num):
  return sum(x for x in xrange(1, max_num) if ((x % 3 == 0) or (x % 5 == 0)))

# multiples_of_3_and_5(1000)
# 233168
