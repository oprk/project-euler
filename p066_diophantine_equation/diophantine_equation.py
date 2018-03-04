# Diophantine equation
# Problem 66
# Consider quadratic Diophantine equations of the form:

# x2 – Dy^2 = 1

# For example, when D=13, the minimal solution in x is 6492 – 13×180^2 = 1.

# It can be assumed that there are no solutions in positive integers when D is square.

# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

# 32 – 2×2^2 = 1
# 22 – 3×1^2 = 1
# 92 – 5×4^2 = 1
# 52 – 6×2^2 = 1
# 82 – 7×3^2 = 1

# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

def is_square(n):
  return int(n**0.5)**2 == n

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

def gcd(a, b):
  while a != 0:
    a, b = b % a, a
  return b

def simplify(numerator, denominator):
  x = gcd(numerator, denominator)
  return ((numerator / x),
          (denominator / x))

class Fraction:

  def __init__(self, numerator, denominator):
    numerator, denominator = simplify(numerator, denominator)
    self.numerator = numerator
    self.denominator = denominator

  def _str_repr(self):
    return "Fraction(numerator={numerator}, denominator={denominator})".format(
      numerator=self.numerator,
      denominator=self.denominator)

  def __str__(self):
    return self._str_repr()

  def __repr__(self):
    return self._str_repr()

  def add(self, fraction):
    return Fraction(((self.numerator * fraction.denominator) +
                     (fraction.numerator * self.denominator)),
                    (self.denominator * fraction.denominator))

  def inv(self):
    return Fraction(self.denominator, self.numerator)

def repeat_generator(repeat_lst):
  while True:
    for elt in repeat_lst:
      yield elt

def continued_fraction(base, repeat_gen, num_iters):
  if num_iters == 0:
    return Fraction(base, 1)
  else:
    return (Fraction(base, 1).add(
      continued_fraction(repeat_gen.next(), repeat_gen, num_iters - 1).inv()))

def minimal_x_diophantine_solution(d):
  base = int(d**0.5)
  repeat_lst = period_square_roots(d)
  iters = 0
  while True:
    gen = repeat_generator(repeat_lst)
    f = continued_fraction(base, gen, iters)
    if (f.numerator ** 2) - (d * (f.denominator ** 2)) == 1:
      return f.numerator
    iters += 1

# minimal_x_diophantine_solution(61)
# 1766319049

best_d = 0
best_value = 0
for i in xrange(1, 1000 + 1):
  if not is_square(i):
    value = minimal_x_diophantine_solution(i)
    if value > best_value:
      best_value = value
      best_d = i
print(best_d)
# 661
