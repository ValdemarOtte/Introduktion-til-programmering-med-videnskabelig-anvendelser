# NOTE : Opgavebeskrivelse
# Exercise 2.1 (sum of two numbers)
# Create a program that asks the user for two numbers and then prints their sum.
# Hint. Use the function input. Recall that the function input returns a str.


def get_int_input() -> int:
    while True:
        val = input("Input: ")
        try:
            return int(val)
        except ValueError:
            print("Dit input skal være et helt tal")


def add(nums=[]) -> int:
    # NOTE : Is better to use: val = sum(nums)
    val = 0
    for num in nums:
        val += num
    return val


if __name__ == '__main__':
    print("Exercise 2.1 (sum of two numbers)")
    print()
    val1 = get_int_input()
    val2 = get_int_input()
    val = add([val1, val2])
    print()
    print(f"{val1} + {val2} = {val}")
