# Power digit sum
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

import time

def digit_sum(num):
  return sum(int(c) for c in str(num))

t0 = time.time()
result = digit_sum(2**1000)
t1 = time.time()

print(result)
print('time %f' % (t1 - t0))
# 1366
# time 0.000255
