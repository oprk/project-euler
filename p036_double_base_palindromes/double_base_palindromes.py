# Double-base palindromes
#
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include
# leading zeros.)

import string
import time

def palindrome(s):
  n = len(s)
  for i in xrange(n / 2 + 1):
    if s[i] != s[(n - 1) - i]:
        return False
  return True

t0 = time.time()
# 1 is palindromic number
total = 1
# Build palindromic binary string.
for i in xrange(1, 10**3):
  s = "{0:b}".format(i)
  rev_s = s[::-1]
  for binary_palindrome in (s + rev_s, s + '0' + rev_s, s + '1' + rev_s):
    dec = int(binary_palindrome, 2)
    if dec < 10**6:
      dec_palindrome = str(dec)
      if palindrome(dec_palindrome):
        print(binary_palindrome, dec_palindrome)
        total += dec
t1 = time.time()

print(total)
print('time %f' % (t1 - t0))
# 872187
# time 0.004788
