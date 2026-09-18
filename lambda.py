# Lambda's example

import math

# Ternary operator. using if else with lambda
# using modulus to detect even or odd on number
oddEven=lambda x:"Even" if x % 2==0 else "Odd"
print(oddEven(4))

# Nested ternary
poin=lambda poin:("a" if poin>=85 else ("b" if poin >=70 and poin <=84 else("c" if poin >=60 and poin <=69 else "d")))
print("Result poin : "+poin(67))

# Dispatcher pattern
# Calculate the square if the number is positive, or the absolute square root if it is negative. 0=positive
number=lambda x: (x ** 2) if x >= 0 else math.sqrt(abs(x))
print(number(2)) # Result 4
print(number(0)) # Result still 0
print(number(-2)) # result 1.4142135....

# Ternary combination with map()
# If the number is less than 0, change it to 0. If it is even, divide by 2. If it is odd, multiply by 3
nl = [-5, 12, 0, 8, -3, 20]
processNl = list(map(lambda x: 0 if x < 0 else (x // 2 if x % 2 == 0 else x * 3),nl))
print(processNl) # Result [0, 6, 0, 4, 0, 10]
