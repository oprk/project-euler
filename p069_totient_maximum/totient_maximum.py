"""
Totient maximum
Problem 69
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n Relatively Prime  φ(n)  n/φ(n)
2	1                 1     2
3	1,2               2     1.5
4	1,3               2     2
5	1,2,3,4           4     1.25
6	1,5               2     3
7	1,2,3,4,5,6       6     1.1666...
8	1,3,5,7           4     2
9	1,2,4,5,7,8       6   	1.5
10	1,3,7,9	4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

"""

def gcd(a, b):
  while a != 0:
    a, b = b % a, a
  return b

def is_relatively_prime(a, b):
  return gcd(a, b) == 1

def phi(n):
  return sum(is_relatively_prime(i, n) for i in xrange(1, n))

max(n / phi(n) for n in xrange(2, 10 + 1))


# https://www.mathblog.dk/project-euler-69-find-the-value-of-n-%E2%89%A4-1000000-for-which-n%CF%86n-is-a-maximum/
# https://en.wikipedia.org/wiki/Euler's_totient_function

def primes(max_num):
  if max_num >= 2:
    prime_bitmap = [True for x in xrange(max_num)]
    prime_bitmap[0] = False
    prime_bitmap[1] = False
    for i in xrange(max_num):
      if prime_bitmap[i]:
        yield i
        for j in xrange(i**2, max_num, i):
          prime_bitmap[j] = False

# This will happen for the number with the most distinct small prime factors. So
# we should be able to construct it by multiplying primes until we reach the
# largest number less then 1.000.000.
def max_phi(limit):
  result = 1
  for p in primes(limit):
    next_result = result * p
    if next_result > limit:
      return result
    else:
      result = next_result

# max_phi(1000000)
# 510510
