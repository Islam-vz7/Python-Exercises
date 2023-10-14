#!/usr/bin/env python3

number = int(input('Enter the Number: '))

def Validate_number(number):
  return 0 <= number <= 100

print(f'{Validate_number(number)}')
