# NOTE : Opgavebeskrivelse
# Exercise 2.4 (integer square root)
# Consider the following program for finding the integer square root of a non-negative integer:
# x = int(input('x: '))
# low = 0
# high = x + 1
# while True:  # low <= sqrt(x) < high
#    if low + 1 == high:
#        break
#    mid = (high + low) // 2
#    if mid * mid <= x:
#        low = mid
#        continue
#    high = mid
# print(low)  # low = floor(sqrt(x))
#    Walk through and understand the program.
#    Try to simplify the program, getting rid of the break and continue statements.

# NOTE : Del 1

x = int(input('x: '))
low = 0
high = x + 1
while True:
    if low + 1 == high:
        break
    mid = (high + low) // 2     # Summer high og low sammen og dividerer det med 2. Herefter runds det ned til første heltal
    if mid * mid <= x:          # Opløfter mid i anden
        low = mid
        continue                # Dette virker som et if-else statement
    high = mid
print(low)



# NOTE : Del 2
from math import sqrt

x = int(input('x: '))
low = 0
high = x + 1
while low + 1 <= sqrt(x) < high:
    mid = (high + low) // 2
    if mid**2 <= x:
       low = mid
    else:
        high = mid
print(low)


