# Digit factorials
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of
# their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import time

fact = {0 : 1}
for i in xrange(1, 10):
  fact[i] = fact[i - 1] * i

def int_to_digits(n):
  lst = []
  while n > 0:
    lst.append(n % 10)
    n /= 10
  return lst

def curious_number(n):
  return n == sum(fact[d] for d in int_to_digits(n))

# Loose upper bound: 7 * 9! < 9999999
t0 = time.time()
result = sum(i for i in  xrange(3, 10**5) if curious_number(i))
t1 = time.time()

print(result)
print('time %f' % (t1 - t0))
# 40730
# time 0.182217

# Check unique combination of digits instead.
def digit_set(min_digit, num_digits):
  if num_digits == 0:
    yield []
  else:
    for i in xrange(min_digit, 10):
      for elt in digit_set(i, num_digits - 1):
        yield [i] + elt

def digit_fact_sum(digits):
  return sum(fact[d] for d in digits)

t0 = time.time()
total = 0
# Use super conservative upper bound of 7 digits.
for i in xrange(8):
  for digits in digit_set(0, i):
    fact_sum = digit_fact_sum(digits)
    if sorted(int_to_digits(fact_sum)) == digits:
      total += fact_sum
t1 = time.time()
# 1! and 2! aren't sums.
print(total - 1 - 2)
print('time %f' % (t1 - t0))
# 40730
# time 0.092734

# If we only check up to 5 digits:
# time 0.011810
