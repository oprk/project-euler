# Cubic permutations
# Problem 62

# The cube, 41063625 (345^3), can be permuted to produce two other cubes:
# 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
# which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.

from collections import defaultdict

# Bin cubes based on their digits until we find a cube with 5 permutations.
def cubic_permutations():
  d = defaultdict(list)
  i = 0
  while True:
    n = i**3
    key = ''.join(sorted(str(n)))

    d[key].append(n)
    if len(d[key]) == 5:
      return min(d[key])

    i += 1

# cubic_permutations()
# 127035954683
