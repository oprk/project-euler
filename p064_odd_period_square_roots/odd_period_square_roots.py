# Odd period square roots
# Problem 64

# All square roots are periodic when written as continued fractions and can be
# written in the form:

# sqrt(n) = a0 + 1 / (a1 + 1 / (a2 + ...))

# It can be seen that the sequence is repeating. For conciseness, we use the
# notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
# indefinitely.

def helper(numerator, n, subtrahend):
  #   numerator / (sqrt(n) - subtrahend)
  # = ((numerator * (sqrt(n) + subtrahend)) /
  #    (n - (subtrahend ** 2)))
  denominator = n - (subtrahend ** 2)
  assert denominator > 0
  # Simplify numerator / denominator
  assert denominator % numerator == 0
  denominator /= numerator

  side_add = int((n**0.5 + subtrahend) / denominator)
  new_subtrahend = side_add * denominator - subtrahend

  # Flip numerator and denominator.
  return (side_add, (denominator, n, new_subtrahend))

def period_square_roots(n):
  a0 = int(n**0.5)
  visited = set([])
  period = []
  state = (1, n, a0)
  while state not in visited:
    visited.add(state)
    side_add, state = helper(*state)
    period.append(side_add)
  return period

def is_square(n):
  return n == int(n**0.5)**2

print(len([1 for i in xrange(10**4 + 1) if not is_square(i) and len(period_square_roots(i)) % 2 == 1]))
# 1322
