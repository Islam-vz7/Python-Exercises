#!/usr/bin/env python3

word = str(input('Enter the word for a check: '))

upper_count = 0
lower_count = 0

for char in word:
  if char.isupper():
    upper_count += 1
  elif char.islower():
    lower_count += 1
print(f'The lowerchases in this word: {lower_count}')
print(f'The upperchases in this word: {upper_count}')

