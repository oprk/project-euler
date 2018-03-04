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

from collections import namedtuple
import math

def is_square(n):
  return int(n**0.5)**2 == n

# def minimal_x_diophantine_solution(d):
#   assert not is_square(d)
#   # Starting with lowest y, increase until there is some x that forms a
#   # Diophantine solution.
#   y = 1
#   while True:
#     dy2 = d * y**2
#     sqrt_dy2 = int(math.ceil((d**0.5) * y))
#     x = sqrt_dy2
#     # print(x, y, (x**2 - dy2))
#     if (x**2 - dy2 == 1):
#       return x
#     y += 1

# for d in xrange(1, 1000):
#   if not is_square(d):
#     print (d, minimal_x_diophantime_solution(d))

# Looks like we're hanging on:
# minimal_x_diophantime_solution(61)

# https://en.wikipedia.org/wiki/Diophantine_equation
# In 1657, Fermat attempted to solve the Diophantine equation 61x2 + 1 = y2 (solved by Brahmagupta over 1000 years earlier). The equation was eventually solved by Euler in the early 18th century, who also solved a number of other Diophantine equations. The smallest solution of this equation in positive integers is x = 226153980, y = 1766319049 (see Chakravala method).
# https://en.wikipedia.org/wiki/Chakravala_method

def gcd(a, b):
  while a != 0:
    a, b = b % a, a
  return b

class DiophantineTuple:

  def __init__(self, x, y, k, d):
    self.x = x
    self.y = y
    self.k = k
    self.d = d

  def _str_repr(self):
    return 'DiophantineTuple(x={x}, y={y}, k={k}, d={d})'.format(
      x=self.x, y=self.y, d=self.d, k=self.k)

  def __str__(self):
    return self._str_repr()

  def __repr__(self):
    return self._str_repr()

  def compose(self, t):
    assert self.d == t.d
    t2 = DiophantineTuple(
      ((self.x * t.x) + (self.d * self.y * t.y)),
      ((self.x * t.y) + (t.x * self.y)),
      (self.k * t.k),
      self.d)
    # Simplfy t2 before returning.
    x = gcd(gcd(t2.x, t2.y), t2.k)
    return DiophantineTuple(t2.x / x, t2.y / x, t2.k / (x ** 2), t2.d)

  def find_m(self):
    # Find m that minimizes |m^2 - d|,
    # such that (x + (y * m)) / k is an integer.
    # (x + (y * m)) = k * i
    m = int(self.d**0.5)
    # Try going both directions when finding m.
    m1 = m
    m2 = m
    while (((self.x + (self.y * m1)) % self.k) != 0 and
           ((self.x + (self.y * m2)) % self.k) != 0):
      m1 += 1
      m2 -= 1
    if (m1 ** 2 - d) < (m2 ** 2 - d):
      return m1
    else:
      return m2

  def apply_bhavana_principle(self):
    if self.k == -1:
      (self.x, self.y) = (((self.x ** 2) + (self.d * (self.y ** 2))),
                          (2 * self.x * self.y))
      self.k = 1
    elif self.k in (-2, 2):
      (self.x, self.y) = ((((self.x ** 2) + (self.d * (self.y ** 2))) / 2),
                          (self.x * self.y))
      self.k = 1
    elif self.k == -4:
      (self.x, self.y) = (((self.x ** 2 + 1) *
                           (((self.x ** 2 + 1) * (self.x ** 2 + 3) / 2) - 1)),
                          ((self.x * self.y * (self.x ** 2 + 1) * (self.x ** 2 + 3)) / 2))
      self.k = 1
    elif self.k == 4:
      if self.x % 2 == 0:
        (self.x, self.y) = (((self.x ** 2 - 2) / 2),
                            (self.y - (self.x * self.y / 2)))
        self.k = 1
      else:
        (self.x, self.y) = ((self.x * (self.x ** 2 - 3) / 2),
                            (self.y * (self.x ** 2 - 1) / 2))
        self.k = 1

  def next(self):
    print(self)
    m = self.find_m()
    t = DiophantineTuple(m, 1, m ** 2 - self.d, self.d)
    t = self.compose(t)
    t.apply_bhavana_principle()
    return t

# t = DiophantineTuple(8, 1, 3, 61)
# while t.k != 1:
#   t = t.next()
# print(t)
# DiophantineTuple(x=1765159286, y=226153980, k=1, d=61)

def minimal_x_diophantine_solution(d):
  print('d: ', d)
  x = int(d**0.5) + 1
  t = DiophantineTuple(x, 1, x ** 2 - d, d)
  while t.k != 1:
    t = t.next()
  return t.x

# print(max(minimal_x_diophantine_solution(i) for i in xrange(1, 100 + 1) if not is_square(i)))

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
