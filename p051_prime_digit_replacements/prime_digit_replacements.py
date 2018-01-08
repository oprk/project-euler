# Prime digit replacements
# Problem 51

# By replacing the 1st digit of the 2-digit number *3, it turns out that six of
# the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
# number is the first example having seven primes among the ten generated
# numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
# 56993. Consequently 56003, being the first member of this family, is the
# smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight prime
# value family.

import copy

def primes(max_num):
  if max_num >= 2:
    prime_bitmap = [True for i in xrange(max_num)]
    prime_bitmap[0] = False
    prime_bitmap[1] = False
    for i in range(max_num):
      if prime_bitmap[i]:
        yield i
        for j in xrange(i**2, max_num, i):
          prime_bitmap[j] = False

# Guess up to 10**6
primes_lst = list(primes(10**6))
primes_set = set(primes_lst)

def int_to_digit_list(n):
  lst = []
  while n > 0:
    lst.append(n % 10)
    n /= 10
  return list(reversed(lst))

def digit_list_to_int(digit_list):
  n = 0
  for digit in digit_list:
    n *= 10
    n += digit
  return n

def replace_digits_prime(prime, digits_index_lst):
  print('replace_digits_prime')
  if not digits_index_lst:
    return 0
  prime_digits = int_digit_list(prime)
  count = 0
  for i in xrange(10):
    new_prime_digits = copy.copy(prime_digits)
    for digit_i in digits_index_lst:
      new_prime_digits[digit_i] = i
    # Leading zeros don't count.
    if new_prime_digits[0] == 0:
      continue
    new_prime = digit_list_to_int(new_prime_digits)
    if new_prime in primes_set:
      print(new_prime)
      count += 1
  print('count: %d' % count)
  return count

assert replace_digits_prime(2, [0]) == 4
assert replace_digits_prime(13, [0]) == 6
assert replace_digits_prime(56003, [2, 3]) == 7

def num_digits(n):
  count = 0
  while n > 0:
    n /= 10
    count += 1
  return count

def all_possible_subsets(collection):
  if not collection:
    yield []
  else:
    car = collection[0]
    cdr = collection[1:]
    for subset in all_possible_subsets(cdr):
      yield subset
      yield [car] + subset

def replace_n_digits(prime):
  n = num_digits(prime)
  return max(replace_digits_prime(prime, digits_index_lst)
             for digits_index_lst in all_possible_subsets(list(xrange(n))))

# for prime in primes_lst:
#   n = replace_n_digits(prime)
#   if n == 8:
#     print(prime, n)
#     break
