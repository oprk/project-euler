# Prime pair sets
# Problem 60

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
# and concatenating them in any order the result will always be prime. For
# example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
# primes, 792, represents the lowest sum for a set of four primes with this
# property.

# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.

import time
from collections import defaultdict

def primes(max_num):
  if max_num >= 2:
    prime_lst = [True] * max_num
    prime_lst[0] = False
    prime_lst[1] = False
    for i in xrange(max_num):
      if prime_lst[i]:
        yield i
        for j in xrange(i**2, max_num, i):
          prime_lst[j] = False

t0 = time.time()
max_num = 100000000
prime_lst = list(primes(max_num))
prime_set = set(prime_lst)
t1 = time.time()

print('prime_lst initialized, time: %f' % (t1 - t0))

def is_prime(num):
  return num in prime_set

def num_digits(num):
  count = 0
  while num != 0:
    count += 1
    num /= 10
  return count

def concat_nums(num1, num2):
  return num1 * 10 ** num_digits(num2) + num2

def split_num(num):
  right = 0
  left = num
  place = 1
  while left > 10:
    digit = left % 10
    right += digit * place
    left /= 10
    place *= 10
    if digit != 0:
      yield (left, right)

prime_concat_pairs = defaultdict(set)

for prime in prime_lst:
  for left, right in split_num(prime):
    if (is_prime(left) and
        is_prime(right) and
        is_prime(concat_nums(right, left))):
      prime_concat_pairs[left].add(right)
      prime_concat_pairs[right].add(left)

print('prime_concat_pairs initialized, time: %f' % (t1 - t0))

def recurse_compatible(candidate_set):
  if len(candidate_set) == 0:
    yield []
  else:
    for prime in candidate_set:
      for rest in recurse_compatible(candidate_set & prime_concat_pairs[prime]):
        yield [prime] + rest

t0 = time.time()
best = None
for prime in prime_lst:
  foo = recurse_compatible(prime_concat_pairs[prime])
  for elt in foo:
    if len(elt) >= 4:
      whole_sequence = [prime] + elt
      s = sum(whole_sequence)
      if best is None or best > s:
        best = s
t1 = time.time()
print best
print('time: %f' % (t1 - t0))

# prime_lst initialized, time: 26.751045
# prime_concat_pairs initialized, time: 26.751045
# [13, 8389, 5701, 6733, 5197] 26033
# time: 15.958320
