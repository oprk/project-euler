# Maximum path sum II
# Problem 67

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

import csv

with open('p067_triangle.txt', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=' ')
  triangle = [[int(elt) for elt in row] for row in reader]

  memo = {}
  def triangle_max_path_sum(row, col):
    if not (row, col) in memo:
      if row < 0 or col < 0 or row < col:
        memo[(row, col)] = 0
      else:
        memo[(row, col)] = (triangle[row][col] +
                            max(triangle_max_path_sum(row - 1, col - 1),
                                triangle_max_path_sum(row - 1, col)))
    return memo[(row, col)]
  last_row = len(triangle) - 1
  num_cols = len(triangle[last_row])
  assert num_cols == len(triangle)
  print(max(triangle_max_path_sum(last_row, col) for col in xrange(num_cols)))
# 7273
