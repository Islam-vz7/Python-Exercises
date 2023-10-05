#!/usr/bin/env python3
  
def Group(Students, GS):
  
  numgroups = int(Students // GS)
  remaining_students = Students % GS
  print(f'There will be {numgroups} groups with {remaining_students} students left over.')

if __name__ == '__main__':

  Students = int(input('How many students? '))
  GS = int(input('Required group size? '))
  Group(Students, GS)
  