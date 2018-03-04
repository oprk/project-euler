# Convergents of e
# Problem 65

# The square root of 2 can be written as an infinite continued fraction.

# The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates
# that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

# It turns out that the sequence of partial values of continued fractions for
# square roots provide the best rational approximations. Let us consider the
# convergents for √2.

# Hence the sequence of the first ten convergents for √2 are:

# 1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

# The first ten terms in the sequence of convergents for e are:

# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
# The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

# Find the sum of digits in the numerator of the 100th convergent of the
# continued fraction for e.

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

# Using 0-indexing:
# continued_fraction(1, repeat_generator([2]), 0)
# Fraction(numerator=1, denominator=1)

# continued_fraction(1, repeat_generator([2]), 1)
# Fraction(numerator=3, denominator=2)

# continued_fraction(1, repeat_generator([2]), 2)
# Fraction(numerator=7, denominator=5)

# continued_fraction(1, repeat_generator([2]), 9)
# Fraction(numerator=3363, denominator=2378)

def e_generator():
  i = 2
  while True:
    yield 1
    yield i
    i += 2
    yield 1

# continued_fraction(2, e_generator(), 10 - 1)
# Fraction(numerator=1457, denominator=536)

def digits(n):
  while n != 0:
    yield n % 10
    n /= 10

print(sum(digits(continued_fraction(2, e_generator(), 100 - 1).numerator)))
# 272
