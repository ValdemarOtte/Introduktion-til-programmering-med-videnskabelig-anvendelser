# NOTE : Opgavebeskrivelse
# Exercise 2.5 (primality test)
# Write a naive program that tests if a small number x ≥ 2 is a prime number.
# Recall that a number is a prime number if and only if the only numbers dividing the number is 1 and the number itself, like the numbers 2, 3, 5, 7, 11, 13...
# The program should ask the user for the number x and print wheter the number is a prime or not. If x is not a prime, it should print a divisor/factor in the range [2, x - 1].
# Hint. Try all relevant factors. Use the % operator to compute the remainder by integer division, e.g. 13 % 5 == 3.


def get_int_input() -> int:
    while True:
        val = input("Input: ")
        try:
            if int(val) >= 2:
                return int(val)
            print("Dit input skal være større eller lig med 2")
        except ValueError:
            print("Dit input skal være et helt tal")


def create_vals(num):
    vals = [2]
    # Find all odd numbers up to half of max_val. Then the half of it because we skip the even numbers
    val = 1
    for idx in range((num // 2) // 2):
        val += 2
        vals.append(val)
    return vals


def check_if_prime(num=int, vals=[]) -> int:
    if num == 2:
        return None, True
    for val in vals:
        if num % val == 0:
            return val, False
    return None, True


if __name__ == '__main__':
    print("Exercise 2.5 (primality test)")
    print()
    num = get_int_input()
    vals = create_vals(num)
    val, prime = check_if_prime(num, vals)
    if prime == True:
        print(f"{num} er et primetal")
    else:
        print(f"{num} er ikke et primetal, da {val} går op i {num}")