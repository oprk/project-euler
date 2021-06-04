"""
Passcode derivation

Problem 79

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""

import re

def match_all_expressions(passcode, expressions):
  for exp in expressions:
    if re.search(exp, passcode) is None:
      return False
  return True

# Simple but slow solution:
def result():
  with open('p079_keylog.txt', 'r') as keylog_file:
    # Create regular expressions
    wildcard = '.*'
    expressions = []
    for line in keylog_file:
      expressions.append(wildcard + wildcard.join(line.strip()) + wildcard)

    for passcode in range(100000000):
      if match_all_expressions(str(passcode), expressions):
        return passcode

# print(result())
#73162890

"""
Congratulations, the answer you gave to problem 79 is correct.

You are the 40818th person to have solved this problem.

This problem has a difficulty rating of 5%. The highest difficulty rating you have solved so far is 30%.

https://projecteuler.net/thread=79
"I did  sort|uniq  and  edited the result."

"I solved this by hand.  The general problem is
topological sorting, which is to embed a given partial
order in a linear order.  See Donald Knuth's The Art
of Computer Programming, Volume 1, Section 2.2.3."

"I also did it by hand. We can easily build a graph where the nodes are the
digits and the edge (u,v) means digit u preceeds v in the passcode. Then do a
topological sort to get the answer. Took < 10 mins. There should be exactly one
way to perform this toposort.  "

We can do topological sort if we assume that the digits don't repeat.

"""

def find_last(edge_map):
  for char in edge_map:
    if not edge_map[char]:
      return char

# Assuming that the passcode doesn't contain repeating characters, we can do a topological sort.
def topological_sort(edge_map):
  reversed_passcode = []
  while edge_map:
    # Find character that doesn't have any other characters after it.  That will
    # be the last character in the passcode.
    char = find_last(edge_map)
    reversed_passcode.append(char)
    edge_map.pop(char)
    # Remove edges to 'char'.
    for other_char in edge_map:
      edge_map[other_char].remove(char)
  return ''.join(reversed(reversed_passcode))

with open('p079_keylog.txt', 'r') as keylog_file:
  # Edge map.
  edge_map = {}
  for line in keylog_file:
    characters = line.strip()
    for i in range(len(characters)):
      char = characters[i]
      if char not in edge_map:
        edge_map[char] = set()
      for after_char in characters[i + 1:]:
        edge_map[char].add(after_char)
  print(edge_map)
  print(topological_sort(edge_map))

# defaultdict(<class 'set'>, {'3': {'0', '1', '6', '2', '8', '9'}, '1': {'0', '6', '2', '8', '9'}, '6': {'0', '2', '9', '8'}, '8': {'9', '0'}, '9': {'0'}, '2': {'9', '8', '0'}, '7': {'0', '1', '3', '6', '2', '8', '9'}})
# 73162890
