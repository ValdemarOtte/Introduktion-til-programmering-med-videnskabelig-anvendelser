# NOTE : Opgavebeskrivelse
# Exercise 2.3 (intersection of two intervals)
# Write a program that determines if two intervals [a, b] and [c, d] overlap, where a ≤ b and c ≤ d. The program should ask the user for the four end-points a, b, c and d of the two intervals, and print if the two intervals overlap or not. If the two intervals overlap, the program should print the interval where the two input intervals overlap.
# Hint. Use one or more if-statements.
# Examples:
# [2, 4] and [6, 9] do not overlap
# [5, 7] and [1, 3] do not overlap
# [4, 8] and [-6, 2] do not overlap
# [2, 5] and [3, 9] overlap in the interval [3, 5]
# [3, 6] and [1, 3] overlap in the interval [3, 3]
# [1, 8] and [2, 6] overlap in the interval [2, 6]


intervals = [
    [[2, 4], [6, 9]],
    [[5, 7], [1, 3]],
    [[4, 8],  [-6, 2]],
    [[2, 5],  [3, 9]],
    [[3, 6],  [1, 3]],
    [[1, 8],  [2, 6]],
]


def check_overlap(interval):
    a, b = interval[0]
    c, d = interval[1]
    # Let the smallest start interval be a and b
    if a > c:
        a, b, c, d = c, d, a, b
    # Check if there is a overlap
    overlap = False
    if b >= c and a <= d:
        overlap = True
        overlap_interval = [c, b]
    elif b <= c and a >= d:
        overlap = True
        overlap_interval = [c, b]
    # If one of the intervals is between the other one
    if a <= c <= b and a <= d <= b:
        overlap_interval = [c, d]
    elif c <= a <= d and c <= b <= d:
        overlap_interval = [a, b]
    if overlap == True:
        print(f"{interval[0]} and {interval[1]} overlap in the interval {overlap_interval}")
    else:
        print(f"{interval[0]} and {interval[1]} do not overlap")



if __name__ == '__main__':
    print("Exercise 2.3 (intersection of two intervals)")
    print()
    for interval in intervals:
        check_overlap(interval)