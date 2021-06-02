"""Prime summations

Problem 77
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five
thousand different ways?

"""

"""This feels like a dynamic programming problem.  Like "how to make change"
for an amount N, with prime values as the coins.

In the example, 7 is the largest prime that can be used in a prime summation for
10.  No primes larger than 10 would be used in a prime summation for 10 of
course.

As the amount we make change for go up in value, we add more prime coins to make
change with.

"""

def primes(max_num):
  if max_num >= 2:
    prime_bitmap = [True for i in range(max_num)]
    prime_bitmap[0] = False
    prime_bitmap[1] = False
    for i in range(max_num):
      if prime_bitmap[i]:
        yield i
        for j in range(i**2, max_num, i):
          prime_bitmap[j] = False


def make_change(value, coins):
  if value < 0:
    return 0
  # Only one way to make value of zero.
  if value == 0:
    return 1
  # Ran out of coins.
  if not coins:
    return 0
  # Either we use the first coin value or we don't.
  return (make_change(value - coins[0], coins) +
          make_change(value, coins[1:]))

"""
My main concern with doing dynamic programming is double counting.
Counting "10 = 7 + 3" and "10 = 3 + 7".

If we keep track of the "largest prime used to form this value", we can avoid
double counting.  For value 9, we wouldn't use any prime larger than 7, so
technically the memo-table that tracks (value, largest_prime_used) wouldn't need
entries for largest_prime_used > value.

Though the memo table would still scale as O(N^2) relative to the value n.

"""

# Coins are sorted from largest to smallest.
memo = {}
def make_change_memoized(value, coins):
  # Only one way to make value of zero.
  if value == 0:
    return 1
  if value < 0:
    return 0
  # Ran out of coins.
  if not coins:
    return 0
  largest_coin = coins[0]
  if (value, largest_coin) not in memo:
    # Either we use the first coin value or we don't.
    memo[(value, largest_coin)] = (make_change_memoized(value - coins[0], coins) +
                                   make_change_memoized(value, coins[1:]))
  return memo[(value, largest_coin)]

max_num = 100
primes = list(primes(max_num))
for value in range(max_num):
  count = make_change_memoized(value, primes)
  print(value, count)

"""
(0, 1)
(1, 0)
(2, 1)
(3, 1)
(4, 1)
(5, 2)
(6, 2)
(7, 3)
(8, 3)
(9, 4)
(10, 5)
(11, 6)
(12, 7)
(13, 9)
(14, 10)
(15, 12)
(16, 14)
(17, 17)
(18, 19)
(19, 23)
(20, 26)
(21, 30)
(22, 35)
(23, 40)
(24, 46)
(25, 52)
(26, 60)
(27, 67)
(28, 77)
(29, 87)
(30, 98)
(31, 111)
(32, 124)
(33, 140)
(34, 157)
(35, 175)
(36, 197)
(37, 219)
(38, 244)
(39, 272)
(40, 302)
(41, 336)
(42, 372)
(43, 413)
(44, 456)
(45, 504)
(46, 557)
(47, 614)
(48, 677)
(49, 744)
(50, 819)
(51, 899)
(52, 987)
(53, 1083)
(54, 1186)
(55, 1298)
(56, 1420)
(57, 1552)
(58, 1695)
(59, 1850)
(60, 2018)
(61, 2198)
(62, 2394)
(63, 2605)
(64, 2833)
(65, 3079)
(66, 3344)
(67, 3630)
(68, 3936)
(69, 4268)
(70, 4624)
(71, 5007)
(72, 5419)
(73, 5861)
(74, 6336)
(75, 6845)
(76, 7393)
(77, 7979)
(78, 8608)
(79, 9282)
(80, 10003)
(81, 10776)
(82, 11603)
(83, 12488)
(84, 13435)
(85, 14445)
(86, 15527)
(87, 16681)
(88, 17914)
(89, 19232)
(90, 20636)
(91, 22134)
(92, 23732)
(93, 25436)
(94, 27251)
(95, 29186)
(96, 31246)
(97, 33439)
(98, 35772)
(99, 38257)


The answer is probably
(71, 5007)

Congratulations, the answer you gave to problem 77 is correct.

You are the 18912th person to have solved this problem.

This problem has a difficulty rating of 25%. The highest difficulty rating you have solved remains at 25%.

Okay, that was kind of easy.
"""
