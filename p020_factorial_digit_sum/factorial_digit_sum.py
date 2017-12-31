# Factorial digit sum
#
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

import operator
import time

t0 = time.time()
result = sum(int(c) for c in str(reduce(operator.mul, xrange(1, 101))))
t1 = time.time()

print(result)
print('time %f' % (t1 - t0))
# 648
# time 0.000105
