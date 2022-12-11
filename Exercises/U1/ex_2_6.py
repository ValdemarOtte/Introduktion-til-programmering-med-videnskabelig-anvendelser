# NOTE : Opgavebeskrivelse
# Exercise 2.6 (integer factorization)
# Write a program that, given a positive integer x, prints the prime factors of that number. Recall that any positive number has a unique prime factorization, e.g. 126 = 2 * 3 * 3 * 7.
# The program should ask the user for the integer x, and then print each prime factor. Note that for x = 126, the prime factor 3 should be printed two times.
# Hint. Repeatedly divide x by 2 until 2 is not a prime factor any longer. Repeat the same for 3, 4, 5,... Note that 4 = 2 * 2 is not a prime number. But since its prime factors cannot be divisors of x divided by the prime factors found so far, then we will not find 4 (and any other composite number) as a prime divisor of x.
from math import gcd


def get_int_input() -> int:
    while True:
        val = input("Input: ")
        try:
            if int(val) >= 1:
                return int(val)
            print("Dit input skal være større eller lig med 1")
        except ValueError:
            print("Dit input skal være et helt tal")


def get_factor(n:int) -> int:
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1
        while factor == 1:
            for idx in range(cycle_size):
                if factor > 1:
                    break
                x = (x * x + 1) % n
                factor = gcd(x - x_fixed, n)
            cycle_size *= 2
            x_fixed = x
        return factor


def factorization(n:int) -> list:
    factors = []
    while n > 1:
        next = get_factor(n)
        factors.append(next)
        n //= next
    factors.sort()
    return factors


if __name__ == '__main__':
    print("Exercise 2.6 (integer factorization)")
    print()
    num = get_int_input()
    print(factorization(num))