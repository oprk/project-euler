"""
Counting fractions in a range
Problem 73

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
"""
import time

# Brute force approach.
# t0 = time.time()
# fractions = set()

# low = 1.0 / 3
# high = 1.0 / 2

# max_num = 12000
# for d in xrange(2, max_num + 1):
#   start_n = d / 3
#   end_n = d / 2
#   for n in xrange(start_n, end_n + 1):
#     f = float(n) / d
#     if low < f and f < high:
#       fractions.add(float(n) / d)

# t1 = time.time()
# print(len(fractions), t1 - t0)
# (7295372, 11.093400955200195)


# http://mathworld.wolfram.com/Stern-BrocotTree.html

# t0 = time.time()
# i = 0

# todo = [(1, 3, 2, 5, 1, 2)]

# for (left_n, left_d, mid_n, mid_d, right_n, right_d) in todo:
#   if mid_d <= 12000:
#     i += 1
#     todo.append((left_n, left_d, left_n + mid_n, left_d + mid_d, mid_n, mid_d))
#     todo.append((mid_n, mid_d, mid_n + right_n, mid_d + right_d, right_n, right_d))
# t1 = time.time()

# print(i, t1 - t0)
# (7295372, 11.371681928634644)
