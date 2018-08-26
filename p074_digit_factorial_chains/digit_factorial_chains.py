"""
Digit factorial chains
Problem 74

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

import operator

def prod(lst):
  return reduce(operator.mul, lst)

digit_fact = {str(i) : prod(xrange(1, i + 1)) for i in xrange(1, 10)}
digit_fact['0'] = 1

def sum_fact(n):
  return sum(digit_fact[c] for c in str(n))

def non_repeating(n):
  seen = set([n])
  m = n
  l = 1
  while True:
    m = sum_fact(m)
    if m not in seen:
      seen.add(m)
      l += 1
    else:
      return l

result = 0
for i in xrange(1000000 + 1):
  x = non_repeating(i)
  if x == 60:
    print(i, x)
    result += 1
print result
# 402

# permutations of:
# 1479
# 4079
# 223974

# 1479 has 4! permutations: 24
# 4079 has 3 * 3 * 2 permutations: 18
# 223974 has 6! / 2! permutations: 360
# 360 + 24 + 18 = 402
