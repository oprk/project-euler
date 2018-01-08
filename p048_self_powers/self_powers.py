# Self powers
# Problem 48

# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

import time

t0 = time.time()
result = str(sum(i**i for i in xrange(1000 + 1)))[-10:]
t1 = time.time()
print(result)
print('time %f' % (t1 - t0))
# 9110846701
# time 0.008385
