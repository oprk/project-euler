# Reciprocal cycles
#
# A unit fraction contains 1 in the numerator. The decimal representation of the
# unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
# seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.

import time

def cycle_length(num):
  while num % 2 == 0:
    num /= 2
  while num % 5 == 0:
    num /= 5
  if num == 1:
    return 0
  i = 1
  while True:
    if (10 ** i - 1) % num == 0:
      return i
    i += 1

t0 = time.time()

best_i = 0
best_cycle = 0
for i in xrange(1, 1000):
  cycles = cycle_length(i)
  if best_cycle < cycles:
    best_cycle = cycles
    best_i = i

t1 = time.time()

print(best_i)
print('time %f' % (t1 - t0))
# 983
# time 0.168501
