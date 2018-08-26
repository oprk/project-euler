"""Totient permutation
Problem 70

Euler's Totient function, phi(n) [sometimes called the phi function], is used to
determine the number of positive numbers less than or equal to n which are
relatively prime to n.

For example, as 1, 2, 4, 5, 7, and 8, are all less than 9 and relatively prime
to 9, phi(9) = 6.

The number 1 is considered to be relatively prime to every positive number, so
phi(1) = 1.

Interestingly, phi(87109) = 79180, and it can be seen that 87109 is a
permutation of 79180.

Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n and
the ratio of n / phi(n) produces a *minimum*.

"""

# The prime factorization of 87109 = 11 * 7919.

# Think of a fast way to compute phi.

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

known_primes = list(primes(5000))
known_primes = [x for x in known_primes if x > 2000]
# len(known_primes)
# 366

# Search over multiple of 2 large primes.
def phi(prime1, prime2):
  return (prime1 - 1) * (prime2 - 1)

def is_permutation(a, b):
  return sorted(str(a)) == sorted(str(b))

i = len(known_primes) - 1
j = len(known_primes) - 1

best_n = 0
best_ratio = 100
for x in known_primes:
  for y in known_primes:
    n = x * y
    p = phi(x, y)
    ratio = float(n) / p
    if n < 10000000 and is_permutation(n, p) and best_ratio > ratio:
      best_n = n
      best_ratio = ratio
print(best_n)
# 8319823
