# Special pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#  a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#
# Find the product abc.

def special_pythagorean_triplet(triplet_sum):
  for a in xrange(1, triplet_sum):
    for b in xrange(a + 1, triplet_sum - a):
      c = triplet_sum - a - b
      if (a**2 + b**2) == c**2:
        return a * b * c
  return None

print(special_pythagorean_triplet(1000))
# 31875000
