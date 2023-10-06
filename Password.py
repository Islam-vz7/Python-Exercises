#!/usr/bin/env python3

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
  Password = input('Create a password: ')
  CPassword = input('Re-enter your password: ')

  if len (Password)<= 12 and len (Password)>=8 and Password not in BAD_PASSWORDS:
    if Password == CPassword:
     print(f'Password Set')
     break
    else:
     print(f'Error')
     print(f'Please try again')
  else:
    print(f'Invalid Password')