# Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
  s = str(num)
  n = len(s)
  for i in xrange(n):
    if s[i] != s[(n - 1) - i]:
      return False
  return True

def palindromes(digits):
  max_digits = (10 ** digits) - 1
  min_digits = 10 ** (digits - 1)
  for i in xrange(max_digits , min_digits - 1, -1):
    for j in xrange(max_digits, i, -1):
      n = i * j
      if is_palindrome(n):
        yield n

print(max(palindromes(3)))
# 906609

