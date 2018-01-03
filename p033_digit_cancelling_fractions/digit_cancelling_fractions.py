# Digit cancelling fractions
#
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
# correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

# (a * 10 + c) / (c * 10 + b) = a / b
# b * (a * 10 + c) = a * (c * 10 + b)

import operator

def gcd(a, b):
  if a > b:
    return gcd(b, a)
  elif a == 0:
    return b
  else:
    return gcd(b % a, a)

fractions = []
for a in xrange(1, 10):
  for b in xrange(1, 10):
    for c in xrange(1, 10):
      if a != b and b * (a * 10 + c) == a * (c * 10 + b):
        print('%d / %d = %d / %d' % (a * 10 + c, c * 10 + b, a, b))
        fractions.append((a, b))

# 16 / 64 = 1 / 4
# 19 / 95 = 1 / 5
# 26 / 65 = 2 / 5
# 49 / 98 = 4 / 8

numerator_prod = reduce(operator.mul, (elt[0] for elt in fractions))
denominator_prod = reduce(operator.mul, (elt[1] for elt in fractions))

print(denominator_prod / gcd(numerator_prod, denominator_prod))
# 100
