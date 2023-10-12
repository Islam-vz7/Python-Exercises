mark_1 = int(input('Enter mark #1: '))
mark_2 = int(input('Enter mark #2: '))
mark_3 = int(input('Enter mark #3: '))
mark_4 = int(input('Enter mark #4: '))
mark_5 = int(input('Enter mark #5: '))

highest = max(mark_1, mark_2, mark_3, mark_4, mark_5)
lowest = min(mark_1, mark_2, mark_3, mark_4, mark_5)
mean = (mark_1 + mark_2 + mark_3 + mark_4 + mark_5) // 5

print(f'The highest mark is: {highest}')
print(f'The lowest mark is: {lowest}')
print(f'The mean mark is: {mean}')

