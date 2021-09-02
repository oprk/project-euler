"""
Path sum: two ways
Submit

 Show HTML problem content
Problem 81
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

# An image is here.  I can enter the values later.

Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

"""

"""
This is a classic dynamic programming problem.
"""

def path_sum(memo, matrix, row, col):
  # If memo hasn't been initialized, make it the same size as the matrix.
  if not memo:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    memo = [[None for i in range(num_cols)] for j in range(num_rows)]

  # If out of bounds, return a base case of 0.
  if (row == -1) or (col == -1):
    return None

  if not memo[row][col]:
    # Look left and above.
    above = path_sum(memo, matrix, (row - 1), col)
    left = path_sum(memo, matrix, row, (col - 1))

    pick = 0
    if above and left:
      pick = min(above, left)
    elif above:
      pick = above
    elif left:
      pick = left

    memo[row][col] = matrix[row][col] + pick

  return memo[row][col]

example = [
  [131, 673, 234, 103, 18],
  [201, 96, 342, 965, 150],
  [630, 803, 746, 422, 111],
  [537, 699, 497, 121, 956],
  [805, 732, 524, 37, 331]
]

# path_sum(None, example, 1, 0)
# 332
# 131 + 201 = 332

# path_sum(None, example, 1, 1)
# 428
# 131 + 201 + 96 = 428

# path_sum(None, example, 1, 2)
# 770
# 131 + 201 + 96 + 342 = 770

# path_sum(None, example, 2, 2)
# 1516
# 131 + 201 + 96 + 342 + 746 = 1516

# 131 + 201 + 96 + 342 + 746 + 422 + 121 + 37 + 331 = 2427

# path_sum(None, example, 4, 4)
# 2427

# Time to load up the actual matrix.

import csv
with open('p081_matrix.txt', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  matrix = [[int(elt) for elt in row] for row in reader]
  rows = len(matrix)
  cols = len(matrix[0])
  result = path_sum(None, matrix, rows - 1, cols - 1)
  print(result)

# 427337
