"""Square root digital expansion

Problem 80

It is well known that if the square root of a natural number is not an integer,
then it is irrational. The decimal expansion of such square roots is infinite
without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the
first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of
the first one hundred decimal digits for all the irrational square roots.
"""

"""https://medium.com/i-math/how-to-find-square-roots-by-hand-f3f7cadf94bb

We only care about the irrational square roots.
So for some numbers like 4, the square root is 2.

We could take the prime factors of a number, and decompose the numbers to XY^2,
where X are all the primes that aren't raised to an even power.

The first one hundred natural numbers is 1-100.  There aren't that many of them.
100 = 2 * 2 * 5 * 5

But what if there are multiple prime factors?
2 * 3 * 5 = 30

What's the square root of 30?
math.sqrt(30)
5.477225575051661

It's probably easiest to actually run the square root digits algorithm.

X = 10A + B
X^2 = (10A + B)^2
= 100A^2 + 2(10AB) + B^2

We want A to be an integer. B can be the floating remainder.
Solve for A.  Find the largest integer A such that 100A^2 < X.

Then find B such that:
20AB + B^2 < X^2 - 100A^2

Then magnify everything by 10

10X = 100A + 10B + C

I guess since we already know A and B, we could just do
D = 10A + B
then 10X = 10D + C
100X^2 = 100D^2 + 20DC + C^2

We already know what D is, so we can focus on calculating C.

With this eventually we can get 100 digits.

"""
def sqrt_digits(x2):
  lst = []
  # x^2 = x2
  # x = 10a + b
  a = 0
  while (100*a**2 < x2):
    a += 1
  # Backtrack one.
  a -= 1
  lst.append(a)
  rest = x2 - 100*a**2
  # print('a =', a)
  # print('rest =', rest)

  for i in range(100):
    b = 0
    while (20*a*b + b**2) < rest:
      b += 1

    # Backtrack one.
    b -= 1
    lst.append(b)
    # print('b =', b)
    rest -= (20*a*b + b**2)
    # print('rest =', rest)
    # Scale up.
    rest *= 100
    # print('rest =', rest)
    a = 10*a + b
  return lst

# sum(sqrt_digits(2))
# 475

squares = [i**2 for i in range(1, 11)]
total = 0
for i in range(1, 101):
  if i not in squares:
    # Irrational.
    result = sum(sqrt_digits(i))
    print(i, result)
    total += result

print(total)
# 40886

# https://projecteuler.net/thread=80
