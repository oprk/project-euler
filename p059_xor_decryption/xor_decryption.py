# XOR decryption
# Problem 59

# Each character on a computer is assigned a unique code and the preferred
# standard is ASCII (American Standard Code for Information Interchange). For
# example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to ASCII,
# then XOR each byte with a given value, taken from a secret key. The advantage
# with the XOR function is that using the same encryption key on the cipher
# text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 =
# 65.

# For unbreakable encryption, the key is the same length as the plain text
# message, and the key is made up of random bytes. The user would keep the
# encrypted message and the encryption key in different locations, and without
# both "halves", it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified
# method is to use a password as a key. If the password is shorter than the
# message, which is likely, the key is repeated cyclically throughout the
# message. The balance for this method is using a sufficiently long password key
# for security, but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower
# case characters. Using cipher.txt (right click and 'Save Link/Target As...'),
# a file containing the encrypted ASCII codes, and the knowledge that the plain
# text must contain common English words, decrypt the message and find the sum
# of the ASCII values in the original text.

import csv
from collections import Counter

key_length = 3

# A XOR K
# B XOR K
# (A XOR K) XOR (B XOR K) = A XOR B

# Space is probably the most common character.

# ord('a') = 97
# ord('z') = 122
# ord(' ') = 32
# Python XOR: 5 ^ 4 = 1

def decrypt_ascii_values(text, key):
  text_length = len(text)
  key_length = len(key)
  key_ord = [ord(elt) for elt in key]
  return [text[i] ^ key_ord[i % key_length]
          for i in xrange(text_length)]

with open('p059_cipher.txt', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  # There is one row with multiple numbers.
  nums = [row for row in reader][0]
  nums = [int(x) for x in nums]
  # Split nums into 3 groups, one for each character in the key
  nums_for_key = [None] * key_length
  key_char_candidate = [None] * key_length
  for key_index in xrange(key_length):
    nums_for_key[key_index] = [nums[i] for i in xrange(len(nums))
                               if i % key_length == key_index]
    most_common_num = Counter(nums_for_key[key_index]).most_common(1)[0][0]
    key_char_candidate[key_index] = chr(most_common_num ^ ord(' '))
  ascii_values = decrypt_ascii_values(nums, key_char_candidate)
  print(''.join(chr(elt) for elt in ascii_values))
  print(sum(ascii_values))

# (The Gospel of John, chapter 1) 1 In the beginning the Word already existed. He was with God, and he was God. 2 He was in the beginning with God. 3 He created everything there is. Nothing exists that he didn't make. 4 Life itself was in him, and this life gives light to everyone. 5 The light shines through the darkness, and the darkness can never extinguish it. 6 God sent John the Baptist 7 to tell everyone about the light so that everyone might believe because of his testimony. 8 John himself was not the light; he was only a witness to the light. 9 The one who is the true light, who gives light to everyone, was going to come into the world. 10 But although the world was made through him, the world didn't recognize him when he came. 11 Even in his own land and among his own people, he was not accepted. 12 But to all who believed him and accepted him, he gave the right to become children of God. 13 They are reborn! This is not a physical birth resulting from human passion or plan, this rebirth comes from God.14 So the Word became human and lived here on earth among us. He was full of unfailing love and faithfulness. And we have seen his glory, the glory of the only Son of the Father.

# 107359
