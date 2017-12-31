# Lattice paths
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

# At each point, we have decision to go right or go down.

def n_choose_k(n, k):
  # n! / (k! * (n - k)!)
  prod = 1
  for i in xrange(k + 1, n + 1):
    prod *= i
  for i in xrange(1, k + 1):
    prod /= i
  return prod

def lattice_paths(grid_rows, grid_cols):
  return n_choose_k(grid_rows + grid_cols, grid_cols)

print(lattice_paths(20, 20))
# 137846528820
