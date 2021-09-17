def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def to_fahrenheit(celsius):
    return 9/5 * celsius + 32

temperature = input('Enter a temperature value: ')
unit = input('Enter the temperature\'s unit: ')

if unit == 'C' or unit == 'c':
    print(f'The temperature is {round(to_fahrenheit(int(temperature)))} F.')
elif unit == 'F' or unit == 'f':
    print(f'The temperature is {round(to_celsius(int(temperature)))} C.')
else:
    print(f"Unit '{unit}' was not recognized as either Celsius or Fahrenheit. Sorry!")
    