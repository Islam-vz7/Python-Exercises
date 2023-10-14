#!/usr/bin/env python3

word = str(input('Enter a word here: '))

def remove_last_char(word):
  if len(word) <= 1:
    return word
  else:
    return word[:-1]
  
print(f'The word is: {word[:-1]}')
