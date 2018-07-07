# Magic 5-gon ring
# Problem 68

# Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

# Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

# It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

# Total	Solution Set
# 9   4,2,3; 5,3,1; 6,1,2
# 9   4,3,2; 6,2,1; 5,1,3
# 10	2,3,5; 4,5,1; 6,1,3
# 10	2,5,3; 6,3,1; 4,1,5
# 11	1,4,6; 3,6,2; 5,2,4
# 11	1,6,4; 5,4,2; 3,2,6
# 12	1,5,6; 2,6,4; 3,4,5
# 12	1,6,5; 3,5,4; 2,4,6

# By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

# Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?

import time

def permutation(lst):
  if not lst:
    yield []
  for i in xrange(len(lst)):
    elt = lst[i]
    rest = lst[:i] + lst[(i+1):]
    for perm_rest in permutation(rest):
      yield [elt] + perm_rest

# Let the first 5 elements in the permutation be the 5 outer numbers.  Make sure
# the first number is the smallest.
def first_smallest(perm):
  return all(perm[0] < elt for elt in perm[1:])

# We need to check whether a permutation is magic.  Figure out the sum of
# numbers on a given ray.  Suppose we had a magic 3-gon [4, 6, 5, 3, 2, 1], like
# in the example.
def ray(outer, inner, index):
  n = len(inner)
  return [outer[index], inner[index], inner[(index + 1) % n]]

def magic(perm):
  n = len(perm) / 2
  outer = perm[:n]
  inner = perm[n:]
  sums = [sum(ray(outer, inner, i)) for i in xrange(n)]
  return len(set(sums)) == 1

def perm_to_string(perm):
  n = len(perm) / 2
  outer = perm[:n]
  inner = perm[n:]
  return "".join(["".join(str(x) for x in ray(outer, inner, i))
                  for i in xrange(n)])

# Find the 5-gon solutions.  Just go backwards and see.
# t0 = time.time()
# n = 5
# for perm in permutation(list(reversed(xrange(1, (n * 2) + 1)))):
#   if first_smallest(perm[:n]) and magic(perm):
#     s = perm_to_string(perm)
#     print perm, s, len(s)
#     break
# t1 = time.time()
# print("time: %f" % (t1 - t0))
# # [6, 10, 9, 8, 7, 5, 3, 1, 4, 2] 6531031914842725 16
# # time: 8.401537

# Not reversed:
# [1, 2, 3, 4, 5, 8, 10, 7, 9, 6] 18102107379496568
# [1, 3, 5, 7, 9, 6, 10, 4, 8, 2] 16103104548782926
# [1, 5, 4, 3, 2, 10, 8, 6, 9, 7] 11085864693972710
# [1, 9, 7, 5, 3, 10, 6, 2, 8, 4] 11069627285843410
# [2, 4, 6, 8, 10, 5, 9, 3, 7, 1] 2594936378711015
# [2, 5, 3, 6, 9, 7, 8, 4, 10, 1] 27858434106101917
# [2, 5, 8, 6, 9, 4, 10, 1, 7, 3] 24105101817673934
# [2, 9, 6, 3, 5, 8, 7, 1, 10, 4] 28797161103104548
# [2, 9, 6, 8, 5, 10, 4, 3, 7, 1] 21049436378715110
# [2, 10, 8, 6, 4, 9, 5, 1, 7, 3] 2951051817673439
# [6, 7, 8, 9, 10, 3, 5, 2, 4, 1] 6357528249411013
# [6, 10, 9, 8, 7, 5, 3, 1, 4, 2] 6531031914842725

# Solution from the forum that is much better than my brute force solution:
t0 = time.time()
constraint = [lambda c: True] * 10
# 10 must be in outer ring, in order for first digit to be max 6.
constraint[0] = lambda c: c[0] == 10
constraint[4] = lambda c: c[0] + c[1] == c[3] + c[4]
constraint[6] = lambda c: c[2] + c[3] == c[5] + c[6]
constraint[8] = lambda c: c[4] + c[5] == c[7] + c[8]
constraint[9] = lambda c: c[6] + c[7] == c[1] + c[9]

sides, rots = [0,1,2,3,2,4,5,4,6,7,6,8,9,8,1], []
for i in range(0, len(sides), 3): rots.append(sides[i:] + sides[:i])

search, sols = [[]], []
while len(search) > 0:
  c = search.pop()
  left = set(range(1, 11)) - set(c)
  # If all numbers are used, we have a magic permutation.
  if len(left) == 0: sols.append(c)
  for cv in left:
    # Add a number from number of digits left, check that the constraint for
    # that position is satisfied so far.  If the constraint is satisfied, the
    # partial solution is appended to the search.
    if constraint[len(c)](c + [cv]): search.append(c + [cv])

for sol in sols:
    sol[:] = min([sol[cidx] for cidx in rot] for rot in rots)

print reduce(lambda a, b: a + b, map(str, max(sols)))
t1 = time.time()
print("time: %f" % (t1 - t0))
# 6531031914842725
# time: 0.018464
