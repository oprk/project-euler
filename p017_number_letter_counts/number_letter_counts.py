# Number letter counts
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
# words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.

number_names = {
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
}


def number_to_words(num):
  # This function is only valid for numbers between 1 to 1000.
  assert 1 <= num and num <= 1000
  thousands = num / 1000
  hundreds = (num % 1000) / 100
  tens = (num % 100) / 10
  ones = (num % 10) / 1
  words = []
  if thousands > 0:
    words.append(number_names[thousands])
    words.append('thousand')
  if hundreds > 0:
    words.append(number_names[hundreds])
    words.append('hundred')
  if (thousands > 0 or hundreds > 0) and (tens > 0 or ones > 0):
    words.append('and')
  if tens == 1:
    words.append(number_names[tens * 10 + ones])
  else:
    if tens >= 2:
      words.append(number_names[tens * 10])
    if ones > 0:
      words.append(number_names[ones])
  return words

print(sum(len(w)
          for i in xrange(1, 1000 + 1)
          for w in number_to_words(i)))
# 21124
