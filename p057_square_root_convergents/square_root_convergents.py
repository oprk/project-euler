# Square root convergents
# Problem 57

# It is possible to show that the square root of two can be expressed as an
# infinite continued fraction.

# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

# By expanding this for the first four iterations, we get:

# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

# The next three expansions are 99/70, 239/169, and 577/408, but the eighth
# expansion, 1393/985, is the first example where the number of digits in the
# numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator
# with more digits than denominator?

from collections import namedtuple

# Fraction = namedtuple('Fraction', ['numerator', 'denominator'], verbose=True)
Fraction = namedtuple('Fraction', ['numerator', 'denominator'], verbose=False)

def gcd(a, b):
  while a > 0:
    (a, b) = (b % a, a)
  return b

def invert_fraction(fraction):
  return Fraction(numerator=fraction.denominator,
                  denominator=fraction.numerator)

def add_fractions(fraction1, fraction2):
  d = fraction1.denominator * fraction2.denominator
  n = ((fraction1.numerator * fraction2.denominator) +
       (fraction2.numerator * fraction1.denominator))
  g = gcd(n, d)
  return Fraction(n / g, d / g)

memo = {}
def square_root_of_two_helper(i):
  if i not in memo:
    if i == 0:
      memo[i] = Fraction(2, 1)
    else:
      memo[i] = add_fractions(Fraction(2, 1),
                              invert_fraction(square_root_of_two_helper(i - 1)))
  return memo[i]

def square_root_of_two(i):
  return add_fractions(Fraction(1, 1),
                       invert_fraction(square_root_of_two_helper(i)))

def num_digits(n):
  count = 0
  while n > 0:
    n /= 10
    count += 1
  return count

count = 0
for i in xrange(1000):
  fraction = square_root_of_two(i)
  if num_digits(fraction.numerator) > num_digits(fraction.denominator):
    count += 1

print count
# 153
