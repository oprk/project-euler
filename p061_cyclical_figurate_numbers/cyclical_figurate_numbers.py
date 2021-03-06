# Cyclical figurate numbers
# Problem 61

# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are
# all figurate (polygonal) numbers and are generated by the following formulae:

# Triangle    P(3,)n=n(n+1)/2   1, 3, 6, 10, 15, ...
# Square      P(4,n)=n^2         1, 4, 9, 16, 25, ...
# Pentagonal  P(5,n)=n(3n−1)/2  1, 5, 12, 22, 35, ...
# Hexagonal	 	P(6,n)=n(2n−1)	 	1, 6, 15, 28, 45, ...
# Heptagonal  P(7,n)=n(5n−3)/2  1, 7, 18, 34, 55, ...
# Octagonal	 	P(8,n)=n(3n−2)	 	1, 8, 21, 40, 65, ...
# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

# The set is cyclic, in that the last two digits of each number is the first two
# digits of the next number (including the last number with the first).

# Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and
# pentagonal (P5,44=2882), is represented by a different number in the set.

# This is the only set of 4-digit numbers with this property.

# Find the sum of the only ordered set of six cyclic 4-digit numbers for which
# each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and
# octagonal, is represented by a different number in the set.

from collections import defaultdict

def triangle(n):
  return n * (n + 1) / 2

def square(n):
  return n ** 2

def pentagonal(n):
  return n * (3 * n - 1) / 2

def hexagonal(n):
  return n * (2 * n - 1)

def heptagonal(n):
  return n * (5 * n - 3) / 2

def octagonal(n):
  return n * (3 * n - 2)

figurate_fn_dict = {
  3: triangle,
  4: square,
  5: pentagonal,
  6: hexagonal,
  7: heptagonal,
  8: octagonal,
}

def num_digits(n):
  count = 0
  while n > 0:
    count += 1
    n /= 10
  return count

# Generate all the n-digit figurate numbers.
def num_digit_figurates(target_num_digits, figurate_fn):
  i = 0
  while True:
    x = figurate_fn(i)
    nd = num_digits(x)

    if nd == target_num_digits:
      # Yield str(integer) because it's easier to check whether it is cyclic
      # later.
      yield str(x)
    elif nd > target_num_digits:
      return

    i += 1

def is_cyclic(str_num_1, str_num_2):
  return str_num_1[2:] == str_num_2[:2]

four_digit_figurate_dict = {i: set(num_digit_figurates(4, figurate_fn_dict[i]))
                            for i in xrange(3, 9)}

# Some figurate numbers can be generated by multiple figurate functions.
# Examples: 9730: [3, 6], 1540: [3, 6]
num_to_figurate_dict = defaultdict(set)
for key, values in four_digit_figurate_dict.items():
  for value in values:
    num_to_figurate_dict[value].add(key)


candidates = set(value
                 for value_lst in four_digit_figurate_dict.values()
                 for value in value_lst)

def search_candidates(path, candidates):
  yield path
  for candidate in candidates:
    if not path or is_cyclic(path[-1], candidate):
      # Remove the figurate classmates of candidate from remaining candidates.
      candidate_figurate_class = num_to_figurate_dict[candidate]
      # There can be multiple classes, so test removing each class of numbers.
      for figurate_class in candidate_figurate_class:
        remaining_candidates = candidates - four_digit_figurate_dict[figurate_class]
        for candidate_path in search_candidates(path + [candidate], remaining_candidates):
          yield candidate_path

# Check paths that are 6 long to see whether they are cyclic.
def cyclic_figurate_numbers():
  for path in search_candidates([], candidates):
    if len(path) == 6 and is_cyclic(path[-1], path[0]):
      return path

# cyclic_figurate_numbers()
# ['5625', '2512', '1281', '8128', '2882', '8256']

result = sum(int(x) for x in cyclic_figurate_numbers())
print result
# 28684
