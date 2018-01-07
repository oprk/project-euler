# Integer right triangles
# Problem 39

# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

from collections import Counter
import time

def squares(max_num):
  i = 1
  while True:
    i2 = i ** 2
    if i2 > max_num:
      break
    yield i2
    i += 1

t0 = time.time()

square_lst = list(squares(1000000))
square_set = set(square_lst)
solutions = Counter()

for a2 in square_lst:
  for b2 in square_lst:
    # Prevent double counting: a >= b
    if b2 > a2:
      break
    c2 = a2 + b2
    if c2 in square_set:
      perimeter = sum(int(x ** 0.5) for x in [a2, b2, c2])
      if perimeter > 1000:
        # Don't increase b anymore, perimeter is already too big.
        break
      solutions[perimeter] += 1

t1 = time.time()

print(solutions.most_common(1)[0][0])
print('time %f' % (t1 - t0))
# 840
# time 0.067051
