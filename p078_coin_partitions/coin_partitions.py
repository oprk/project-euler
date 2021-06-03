"""
Coin partitions

Problem 78

Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.

"""


"""
Brainstorming:
This is like the "make-change" problem, except we can make change with all integers.


https://en.wikipedia.org/wiki/Partition_(number_theory)
No closed-form expression for the partition function is known, but it has both asymptotic expansions that accurately approximate it and recurrence relations by which it can be calculated exactly.

The multiplicative inverse of its generating function is the Euler function; by Euler's pentagonal number theorem this function is an alternating sum of pentagonal number powers of its argument.

p(n)=p(n-1)+p(n-2)-p(n-5)-p(n-7)+...

What are "pentagonal numbers"?
https://en.wikipedia.org/wiki/Pentagonal_number
pentagonal(n) = (3*n^2 - n) / 2

"""

def pentagonal(n):
  return (3*n**2 - n) / 2

# [pentagonal(n) for n in range(10)]
# [0, 1, 5, 12, 22, 35, 51, 70, 92, 117]

# I don't see the number "2" or "7".
# https://en.wikipedia.org/wiki/Pentagonal_number_theorem
# for k = 1, −1, 2, −2, 3

# [pentagonal(i) for i in [1, -1, 2, -2, 3, -3]]
# [1, 2, 5, 7, 12, 15]
# Got it!  It's the "generalized pentagonal sequence".

memo = {}

def count_partitions(n):
  if n == 0:
    return 1
  if n < 0:
    return 0
  if n not in memo:

    # Alternating sum of pentagonal numbers.
    # i = 1, -1, 2, -2, 3, -3, ...
    total = 0
    i = 1
    while True:
      alt_scale = 1 if (i % 2) == 1 else -1

      a = pentagonal(i)
      if a > n:
        break
      total += alt_scale * count_partitions(n - a)

      b = pentagonal(-i)
      if b > n:
        break
      total += alt_scale * count_partitions(n - b)

      i += 1

    memo[n] = total

  return memo[n]

i = 1
while True:
  if (count_partitions(i) % 1000000) == 0:
    print(i)
    break
  i += 1

# 55374

"""
Congratulations, the answer you gave to problem 78 is correct.

You are the 16608th person to have solved this problem.

This problem has a difficulty rating of 30%. The highest difficulty rating you had previously solved was 25%.
This is a new record. Well done!
"""
