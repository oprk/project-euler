# Sub-string divisibility
# Problem 43

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
# each of the digits 0 to 9 in some order, but it also has a rather interesting
# sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
# the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.

import time

def permutations(collection):
  if not collection:
    yield collection
  else:
    for i in xrange(len(collection)):
      elt = collection[i]
      rest_collection = collection[:i] + collection[(i + 1):]
      for perm in permutations(rest_collection):
        yield [elt] + perm

def int_digits_to_int(digit_lst):
  n = 0
  for digit in digit_lst:
    n = n * 10 + digit
  return n

# t0 = time.time()
# total = 0
# for perm in permutations(list(xrange(10))):
#   # Don't count pandigitals with 0 most significant digit.
#   if perm[0] == 0:
#     continue
#   if (int_digits_to_int(perm[i] for i in [7, 8, 9]) % 17 == 0 and
#       int_digits_to_int(perm[i] for i in [6, 7, 8]) % 13 == 0 and
#       int_digits_to_int(perm[i] for i in [5, 6, 7]) % 11 == 0 and
#       int_digits_to_int(perm[i] for i in [4, 5, 6]) % 7 == 0 and
#       int_digits_to_int(perm[i] for i in [3, 4, 5]) % 5 == 0 and
#       int_digits_to_int(perm[i] for i in [2, 3, 4]) % 3 == 0 and
#       int_digits_to_int(perm[i] for i in [1, 2, 3]) % 2 == 0):
#     x = int_digits_to_int(perm)
#     print(x)
#     total += x
# t1 = time.time()
# print(total)
# print('time %f' % (t1 - t0))
# # 1406357289
# # 1430952867
# # 1460357289
# # 4106357289
# # 4130952867
# # 4160357289
# # 16695334890
# # time 19.837629

def digit_multiples(prime, max_digits):
  i = 1
  n = prime
  max_num = 10 ** max_digits - 1
  while n < max_num:
    digits = str(n)
    # Pad to correct number of zeros.
    digits = '0' * (max_digits - len(digits)) + digits
    yield digits
    i += 1
    n += prime

def digit_overlap(num_digits, str1, str2):
  return str1[-num_digits:] == str2[:num_digits]

def helper(primes, ending):
  if not primes:
    yield ending
  else:
    prime = primes[0]
    rest_primes = primes[1:]
    for digits in digit_multiples(prime, 3):
      if not ending or digit_overlap(2, digits, ending):
        new_ending = digits[0] + ending if ending else digits
        # Digits are unique so far.
        if len(set(new_ending)) == len(new_ending):
          for new_digits in helper(rest_primes, new_ending):
            yield new_digits

t0 = time.time()
# First digit is unconstrained, can be whatever; so add 1 to primes list.
lst = list(helper([17, 13, 11, 7, 5, 3, 2, 1], ''))
result = sum(int(i) for i in lst)
t1 = time.time()
print(result)
print('time %f' % (t1 - t0))
# 16695334890
# time 0.013977
