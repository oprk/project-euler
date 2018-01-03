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

pandigital_set = [str(i) for i in xrange(1, 10)]

def pandigital_product(a, b):
  c = a * b
  s = str(a) + str(b) + str(c)
  return sorted(s) == pandigital_set

assert pandigital_product(39, 186)

def assign_groups(num_elts, num_groups):
  if num_elts == 0:
    yield []
  else:
    for group in assign_groups(num_elts - 1, num_groups):
      for i in xrange(num_groups):
        yield [i] + group

def split_group_helper(collection, num_groups, assignment):
  assert len(collection) == len(assignment)
  z = zip(collection, assignment)
  return [[elt for (elt, group) in z if group == target_group]
          for target_group in xrange(num_groups)]

def split_groups(collection, num_groups):
  for assignment in assign_groups(len(collection), num_groups):
    yield split_group(collection, num_groups, assignment)

def digits_to_int(collection):
  result = 0
  for elt in collection:
    result *= 10
    result += elt
  return result

def smallest_value(collection):
  return digits_to_int(sorted(collection))

def largest_value(collection):
  return digits_to_int(reversed(sorted(collection)))

def permutation(collection):
  if not collection:
    yield []
  for elt in collection:
    rest = list(collection)
    rest.remove(elt)
    for rest_perm in permutation(rest):
      yield [elt] + rest_perm

def generate_pandigital_products():
  prods = set()
  collection = xrange(1, 10)
  num_groups = 3
  for [a, b, c] in split_groups(collection, num_groups):
    # a, b, c should contain digits.
    if (not a) or (not b) or (not c):
      continue
    # To break symmetry and avoid double counting, let a have smaller smallest digit.
    if a[0] > b[0]:
      continue
    if len(c) < (len(a) + len(b) - 1):
      continue
    # Smallest possible value for a, b should be smaller than largest possible
    # value for c.
    largest_c = largest_value(c)
    if smallest_value(a) > largest_c or smallest_value(b) > largest_c:
      continue
    for a_digits in permutation(a):
      a_int = digits_to_int(a_digits)
      for b_digits in permutation(b):
        b_int = digits_to_int(b_digits)
        if pandigital_product(a_int, b_int):
          prod = a_int * b_int
          prods.add(prod)
  return sum(prods)

t0 = time.time()
result = generate_pandigital_products()
t1 = time.time()

print(result)
print('time %f' % (t1 - t0))
# 45228
# time 0.277365
