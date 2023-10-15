#!/usr/bin/env python3
from statistics import mean

#if __name__ == '__main__':
#  celsius = float(input('Enter the temperature in Celsius: '))
#  Fahrenheit = celsius * 1.8 + 32
#  print(f'{celsius}C is equivalent to {Fahrenheit}F')


count = int(input('How many temperatures will you type ? '))

temperatures = []
for i in range(count):
    temperature = input('Enter the temperature: ')
    if not temperature:
        print('Exiting...')
        exit()

    temperatures.append(temperature)

highest = max(temperatures)
lowest = min(temperatures)
mean = mean(temperatures)

print(f'Maximum temperature is: {highest}')
print(f'Minimum temperature is: {lowest}')
print(f'Mean of the temperatures is: {mean}')


# unit = input('Is this temperature in C(Celsius) or F(Fahrenheit) ? ')


#if unit == 'C' or unit == 'c':
#  temperature_converted = (temperature * 1.8) + 32
#  unit_converted = 'F'
#elif unit == 'F' or unit == 'f':
#  temperature_converted = (temperature - 32) * 5/9
#  unit_converted = 'C'
#else:
#  print(f'Invalid Unit. Please enter the unit again')
#  exit()


#print(f'The temperature selected: {temperature} {unit.upper()}')
#print(f'The temperature selected: {temperature_converted} {unit_converted}')

