# NOTE : Opgavebeskrivelse
# Exercise 2.7* (Newton-Raphson square root)
# Use the Newton-Raphson method to compute the square root of a float n ≥ 1.0, by finding a root of the function f(x) = x2 - n and letting your initial approximation of the root be x = n. Recall f'(x) = 2 * x. In your computaions you can use +, -, *, and /.
# You can compare your result to the result of the builtin sqrt function in the math module using:
# import math
# print(math.sqrt(n))
import math


def f(x, n):
    # f(x) = x^2 - n
    return x**2 - n


def dfdx(x):
    # f'(x) = 2x
    return 2*x


def newton_raphson(x, n, count):
    for idx in range(10):
        x -= f(x, n) / dfdx(x)
        print(f"{idx+1}: {x}")
    return x


x = 16
n = x
count = 10

x = newton_raphson(x, n, count)
print(f"Kvadratroden af {n} er {math.sqrt(n)}. Vha. Newton Raphson metoden kom vi frem til {x}")