# Number spiral diagonals
#
# Starting with the number 1 and moving to the right in a clockwise direction a
# 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?

def number_spiral_diagonals(n):
  # n should be odd, otherwise there would be no center to start from.
  assert n % 2 == 1
  iters = (n - 1) / 2
  a = 1
  yield a
  for i in xrange(1, iters + 1):
    for j in xrange(4):
      a += 2 * i
      yield a

assert sum(number_spiral_diagonals(5)) == 101

print sum(number_spiral_diagonals(1001))
# 669171001
