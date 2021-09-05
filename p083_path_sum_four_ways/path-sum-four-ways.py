"""Path sum: four ways

Problem 83
NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom
right, by moving left, right, up, and down, is indicated in bold red and is
equal to 2297.


Find the minimal path sum from the top left to the bottom right by moving left,
right, up, and down in matrix.txt (right click and "Save Link/Target As..."), a
31K text file containing an 80 by 80 matrix.

"""

"""I'm going to straight up use A* search for this problem.
I will construct a graph that represents the matrix.

Each cell of the matrix is a node.  When you "enter" a cell, from any of the
four directions (left, right, up, down), you "pay" the cost of the number in the
cell.

I don't even need to use an adjacency list to represent the graph, because the
graph is derived from a 2D matrix.

Each node is represented as (row, col).

We have a cost dictionary (the matrix):
matrix[node] = cost


We can look up the cost of traversing the edge by looking up the cost of the
destination node in the matrix.

A* search is like a flood-fill from the source (or goal node, it doesn't
matter), extending the shortest known path from the source node first, until the
goal node is reached.

For generic search, we need:

- visited list (optional).  This prevents us from choosing a shortest path with
  negative edges that cycle forever.

- "next" (next path to extend function).  In breadth-first-search, we visit
  siblings of the current node before we visit the children of the current node.
  In depth-first-search, we visit children of the current node before we visit
  siblings of the current node. In A* search, we extend the shortest known path
  originating from the source node.

If we have a node in the path_queue, and we extend it, and then see the *same node* again, what's the cost to traverse to that node?  That's a cycle by definition.  It seems like the first time we see a node, we've taken the shortest path to that node (because we are floodfilling by cost from the source node).  What about the second time we see a node?  Then we've taken a longer path to see that node.  We probably don't want to take that longer path, or it doesn't count or something.  Should we just delete it and not put it in the path_queue, while keeping the shorter path?  I think deleting the new longer path would cause us to have a loop in our algorithm; we'll keep picking up the short path, extending it, ignoring the longer path.  A node with a self-loop would get picked over and over again from the path_queue.  We need to discard the shorter path from the path_queue after we extend it.

Let's start path_queue as DFS, so it's just a list:
[node: <shortest path from source>]
= [node:(cost of shortest path from source, [nodes in path])]

We can skip the [nodes in path] part; that's something we could track later if we wanted to.


"""

import collections
import copy
import csv
import heapq

Node = collections.namedtuple('Node', ['row', 'col'])

example = [
  [131, 673, 234, 103, 18],
  [201, 96, 342, 965, 150],
  [630, 803, 746, 422, 111],
  [537, 699, 497, 121, 956],
  [805, 732, 524, 37, 331]
]


def search(matrix, src_node, dst_node):
  num_rows = len(matrix)
  num_cols = len(matrix[0])

  # Didn't have numpy.inf available, throw in a big number just to solve this Project Euler problem quickly.
  min_cost_from_source = [[1000000 for i in range(num_cols)] for j in range(num_rows)]

  # Extend a path by finding the neighbors of the last node in the path.
  def neighbors(node):
    row = node.row
    col = node.col
    # Each cell has up to 4 neighbors: left, right, up, down.
    if row > 0:
      yield Node(row - 1, col)
    if col > 0:
      yield Node(row, col - 1)
    if row < (num_rows - 1):
      yield Node(row + 1, col)
    if col < (num_cols - 1):
      yield Node(row, col + 1)

  # Seed the path_queue with the source node.
  # heapq heap is a "min heap", returning the smallest item.
  path_queue = [(matrix[src_node.row][src_node.col], src_node)]
  heapq.heapify(path_queue)
  while path_queue:
    path = heapq.heappop(path_queue)
    path_cost, last_path_node = path
    # Are we there yet?
    if last_path_node == dst_node:
      print('Arrived!', path_cost)
      return path_cost
    for neighbor in neighbors(last_path_node):
      edge_cost = matrix[neighbor.row][neighbor.col]
      extended_path_cost = (path_cost + edge_cost)
      if min_cost_from_source[neighbor.row][neighbor.col] >= extended_path_cost:
        # Found new minimum path to this neighbor node!  Worth extending this path further.
        # This "if" check is to save space in the heap and avoid adding paths we won't use.
        min_cost_from_source[neighbor.row][neighbor.col] = extended_path_cost
        heapq.heappush(path_queue, (extended_path_cost, neighbor))
  assert(False)

# search(example, Node(4, 4), Node(4, 4))
# 331

# search(example, Node(4, 3), Node(4, 4))
# 368 = 331 + 37

# search(example, Node(3, 3), Node(4, 4))
# 489 = 331 + 37 + 121

# search(example, Node(2, 3), Node(4, 4))
# 911 = 331 + 37 + 121 + 422

# search(example, Node(2, 4), Node(4, 4))
# 1022 = 331 + 37 + 121 + 422 + 111

# search(example, Node(1, 4), Node(4, 4))
# 1172 = 331 + 37 + 121 + 422 + 111 + 150

# search(example, Node(0, 4), Node(4, 4))
# 1190 = 331 + 37 + 121 + 422 + 111 + 150 + 18

# search(example, Node(0, 3), Node(4, 4))
# 1293 = 331 + 37 + 121 + 422 + 111 + 150 + 18 + 103

# search(example, Node(0, 2), Node(4, 4))
# 1527 = 331 + 37 + 121 + 422 + 111 + 150 + 18 + 103 + 234

# search(example, Node(1, 2), Node(4, 4))
# 1869 = 331 + 37 + 121 + 422 + 111 + 150 + 18 + 103 + 234 + 342

# search(example, Node(0, 0), Node(4, 4))
# 2297
# Everything seems to work so far.

with open('p083_matrix.txt', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  matrix = [[int(elt) for elt in row] for row in reader]
  num_rows = len(matrix)
  num_cols = len(matrix[0])
  r = search(matrix, Node(0, 0), Node(num_rows - 1, num_cols - 1))
  print(r)
# 425185
# https://projecteuler.net/thread=83
