#!/usr/bin/env python3

while True:
  
  Password = input('Create a password: ')
  CPassword = input('Confirm your password: ')

  if Password == CPassword:
    print(f'Password Set')
    break
  else:
    print(f'Error')
    print(f'Please try again')  
