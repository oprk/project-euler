# Powerful digit counts
# Problem 63

# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
# number, 134217728=8^9, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

def num_digits(x):
  count = 0
  while x > 0:
    x /= 10
    count += 1
  return count

# n digits and an nth power
def powerful_digit_count(n):
  i = 1
  # Initialize it to some value s.t. d < n.
  d = 0
  while d <= n:
    x = i ** n
    d = num_digits(x)
    if d == n:
      yield x
    i += 1

def powerful_digit_counts():
  i = 1
  total = 0
  # Initialize it to some positive value.
  count = 1
  while count > 0:
    count = len(list(powerful_digit_count(i)))
    total += count
    i += 1
  return total

# powerful_digit_counts()
# 49
