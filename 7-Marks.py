from statistics import mean


#mark_1 = int(input('Enter mark #1: '))
#mark_2 = int(input('Enter mark #2: '))
#mark_3 = int(input('Enter mark #3: '))
#mark_4 = int(input('Enter mark #4: '))
#mark_5 = int(input('Enter mark #5: '))
#
#highest = max(mark_1, mark_2, mark_3, mark_4, mark_5)
#lowest = min(mark_1, mark_2, mark_3, mark_4, mark_5)
#mean = (mark_1 + mark_2 + mark_3 + mark_4 + mark_5) // 5
#
#print(f'The highest mark is: {highest}')
#print(f'The lowest mark is: {lowest}')
#print(f'The mean mark is: {mean}')
#
#

number_of_marks = int(input('How many marks do you want to enter? '))
marks = []
for i in range(number_of_marks):
    mark = int(input('Enter mark: '))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
mean = mean(marks)

print(f'The highest mark is: {highest}')
print(f'The lowest mark is: {lowest}')
print(f'The mean mark is: {mean}')

