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
# ('11', '3')
# ('101', '5')
# ('111', '7')
# ('1001', '9')
# ('100001', '33')
# ('1100011', '99')
# ('100111001', '313')
# ('1001001001', '585')
# ('1011001101', '717')
# ('1110100010111', '7447')
# ('10001100110001', '9009')
# ('11101111110111', '15351')
# ('111110111011111', '32223')
# ('10010000000001001', '73737')
# ('1001110000111001', '39993')
# ('1100111111110011', '53235')
# ('1101001001001011', '53835')
# ('10001110111101110001', '585585')

# 872187
# time 0.004788

# Compare with brute force example, just in case.
t0 = time.time()
result = sum(i for i in xrange(1, 10**6)
             if palindrome(str(i)) and palindrome("{0:b}".format(i)))
t1 = time.time()
print(result)
print('time %f' % (t1 - t0))
# 872187
# time 0.570948
