# Coded triangle numbers
# Problem 42

# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
# the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value. For
# example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
# is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
# containing nearly two-thousand common English words, how many are triangle
# words?

import csv
import time

def word_value(word):
  base = ord('A') - 1
  return sum(ord(c) - base for c in word)

assert word_value('SKY') == 55

def triangle_numbers(max_num):
  i = 0
  n = 0
  while n < max_num:
    i += 1
    n = i * (i + 1) / 2
    yield n

t0 = time.time()
with open('words.txt', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='"')
  # There is one row with multiple words.
  words = [row for row in reader][0]
  max_num = max(word_value(word) for word in words)
  triangle_set = set(triangle_numbers(max_num))
  total = sum(1 for word in words if word_value(word) in triangle_set)
t1 = time.time()
print(total)
print('time %f' % (t1 - t0))
# 162
# time 0.004390
