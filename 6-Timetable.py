#!/usr/bin/env python3

while True:

  number = int(input('Enter the number to show its timetable: '))
  
  if 0 <= number <=12:
    for i in range(13):
        result = int(i * number)

        print(f'{i} x {number} = {result}')

  else:
      for i in range(12,0,-1):
        result = int(i * number/-1)

        print(f'{i} x {int(number/-1)} = {result}')
        