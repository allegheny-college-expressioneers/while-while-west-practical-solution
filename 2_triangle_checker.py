def is_equilateral(a, b, c):
    return a == b == c

def is_isosceles(a, b, c):
    return a == b or b == c or c == a

def is_scalene(a, b, c):
    return a != b and b != c and c != a

a = input('Enter the length of the first side: ')
b = input('Enter the length of the second side: ')
c = input('Enter the length of the third side: ')

if is_equilateral(a, b, c):
    print('Triangle is equilateral!')
if is_isosceles(a, b, c):
    print('Triangle is isosceles!')
if is_scalene(a, b, c):
    print('Triangle is scalene!')

# Another correct implementation, but with slightly different behavior:
# It won't tell you that equilateral triangles are also isosceles triangles

if is_equilateral(a, b, c):
    print('Triangle is equilateral!')
elif is_isosceles(a, b, c):
    print('Triangle is isosceles!')
else:
    print('Triangle is scalene!')
