# 1000-digit Fibonacci number
#
# The Fibonacci sequence is defined by the recurrence relation:
#
# F(n) = F(n−1) + F(n−2), where F(1) = 1 and F(2) = 1.
# Hence the first 12 terms will be:
#
# F(1) = 1
# F(2) = 1
# F(3) = 2
# F(4) = 3
# F(5) = 5
# F(6) = 8
# F(7) = 13
# F(8) = 21
# F(9) = 34
# F(10) = 55
# F(11) = 89
# F(12) = 144
# The 12th term, F(12), is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import time

def fib(digits):
  (a, b) = 1, 1
  max_num = 10**(digits - 1)
  i = 2
  while b < max_num:
    (a, b) = (b, a + b)
    i += 1
  return i

t0 = time.time()
result = fib(1000)
t1 = time.time()

print(result)
print('time %f' % (t1 - t0))
# 4782
# time 0.000838
