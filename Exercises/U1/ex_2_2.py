# NOTE : Opgavebeskrivelse
# Exercise 2.2 (sum of k numbers)
# Create a program that adds a user specified number of numbers. The program should first ask the user for a number k, then ask the user for the k numbers to add, and finally print the sum of the k numbers.
# Hint. Use a while-loop.


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


def join_ints(vals=[], between=str) -> str:
    strs = []
    for val in vals:
        strs.append(str(val))
    return f'{between}'.join(strs)


if __name__ == '__main__':
    print("Exercise 2.2 (sum of k numbers)")
    print()
    print("Antal tal du vil summe sammen")
    k = get_int_input()
    print()
    vals = []
    for idx in range(k):
        val = get_int_input()
        vals.append(val)
    val = add(vals)
    print()
    cal = join_ints(vals, " + ")
    print(f"{cal} = {val}")
