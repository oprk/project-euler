# 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def primes(max_num):
  if max_num >= 2:
    prime_bitmap = [True for i in xrange(max_num)]
    prime_bitmap[0] = False
    prime_bitmap[1] = False
    for i in xrange(max_num):
      if prime_bitmap[i]:
        yield i
        for j in xrange(i**2, max_num, i):
          prime_bitmap[j] = False

def nth_prime(n):
  # Use iterative-deepening approach to find primes.
  iteration = 0
  while True:
    iteration += 1
    count = 0
    for prime in primes(2**iteration):
      count += 1
      if count == n:
        return prime

print(nth_prime(10001))
# 104743

# iteration: 17
