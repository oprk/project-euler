"""
Path sum: three ways

Problem 82
NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.


Find the minimal path sum from the left column to the right column in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

"""We need to make sure we only visit each cell once.  Because we can move both
up and down, we can accidentally go in a loop.  We could restrict the column
direction to prevent loops.  If the path is already going up the column, you
have to keep going up, and you can't go down.

direction: the direction we enter the cell in, for the minimum path.

"""

import csv
from enum import Enum

class Direction(Enum):
  ABOVE = 1
  BELOW = 2
  LEFT = 3

def path_sum(memo, matrix, row, col, direction):
  # If memo hasn't been initialized, make it the same size as the matrix.
  num_rows = len(matrix)
  num_cols = len(matrix[0])

  # If out of bounds, return a base case of 0.
  if (row < 0) or (col < 0) or (row >= num_rows) or (col >= num_cols):
    return None

  if (row == 0 and direction == Direction.ABOVE):
    # There's nothing above row 0.  We can't enter the cell from that direction.
    return None
  if (col == 0 and direction == Direction.LEFT):
    # There's nothing to the left of column 0.  That's the starting point.
    return matrix[row][col]

  if (row == (num_rows - 1) and direction == Direction.BELOW):
    # There's nothing below the last row.  We can't enter the cell from that direction.
    return None

  if (row, col, direction) not in memo:
    # Look left, above, and below.
    candidates = []
    # We can always enter the current cell from the left.  No danger of looping
    # here, because we are always traveling from left to right, and never right
    # to left.
    for d in Direction:
      candidates.append(path_sum(memo, matrix, row, (col - 1), d))

    if direction == Direction.ABOVE:
      # We're restricted to enter the current cell from above.
      for d in (Direction.ABOVE, Direction.LEFT):
        candidates.append(path_sum(memo, matrix, (row - 1), col, d))

    if direction == Direction.BELOW:
      # We're restricted to enter the current cell from below.
      for d in (Direction.BELOW, Direction.LEFT):
        candidates.append(path_sum(memo, matrix, (row + 1), col, d))

    # Filter out the invalid (out of bounds) candidates.
    candidates = [elt for elt in candidates if elt]
    pick = 0
    if candidates:
      pick = min(candidates)

    memo[(row, col, direction)] = matrix[row][col] + pick

  return memo[(row, col, direction)]

example = [
  [131, 673, 234, 103, 18],
  [201, 96, 342, 965, 150],
  [630, 803, 746, 422, 111],
  [537, 699, 497, 121, 956],
  [805, 732, 524, 37, 331]
]

# path_sum({}, example, 0, 0, Direction.LEFT)
# 131

# path_sum({}, example, 1, 0, Direction.LEFT)
# 201

# path_sum({}, example, 1, 1, Direction.LEFT)
# 297
# 201 + 96 = 297

# path_sum({}, example, 1, 0, Direction.ABOVE)
# 332
# 131 + 201 = 332

# path_sum({}, example, 1, 2, Direction.LEFT)
# 639
# 201 + 96 + 342 = 639

# path_sum({}, example, 0, 2, Direction.BELOW)
# 873
# 201 + 96 + 342 + 234 = 873

# path_sum({}, example, 0, 4, Direction.LEFT)
# 994
# Just like in the example matrix image on the project euler webpage.

# Now we just need to go to the last column and find the minimum path.
def result(matrix):
  candidates = []
  memo = {}
  num_rows = len(matrix)
  num_cols = len(matrix[0])
  for row in range(num_cols):
    for direction in Direction:
      r = path_sum(memo, matrix, row, (num_cols - 1), direction)
      if r:
        candidates.append(r)
  return min(candidates)

# print(result(example))
# 994

with open('p082_matrix.txt', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  matrix = [[int(elt) for elt in row] for row in reader]
  num_rows = len(matrix)
  num_cols = len(matrix[0])
  print(len(matrix))
  r = result(matrix)
  print(r)
# 260324

# https://projecteuler.net/thread=82
