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
with open('p079_keylog.txt', 'r') as keylog_file:
  # Create regular expressions
  wildcard = '.*'
  expressions = []
  for line in keylog_file:
    expressions.append(wildcard + wildcard.join(line.strip()) + wildcard)

  for passcode in range(100000000):
    if match_all_expressions(str(passcode), expressions):
      print(passcode)
      break

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
