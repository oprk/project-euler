# Powerful digit sum
# Problem 56

# A googol (10^100) is a massive number: one followed by one-hundred zeros;
# 100^100 is almost unimaginably large: one followed by two-hundred
# zeros. Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what is the
# maximum digital sum?

def digit_sum(n):
  return sum(int(c) for c in str(n))

print(max(digit_sum(a**b)
          for a in xrange(100)
          for b in xrange(100)))
# 972
