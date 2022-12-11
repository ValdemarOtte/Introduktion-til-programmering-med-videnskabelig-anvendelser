# NOTE : Opgavebeskrivelse
# Exercise 4.6 (multiplication table)
# Print a multiplication table of a given dimension. Below is shown the multiplication table for dimension 7. The program should ask the user to input the dimension of the table (≤ 100), and then print a multiplication table where all entries in a column are right aligned.
#
#  * |  0  1  2  3  4  5  6  7
#-----------------------------
#  0 |  0  0  0  0  0  0  0  0
#  1 |  0  1  2  3  4  5  6  7
#  2 |  0  2  4  6  8 10 12 14
#  3 |  0  3  6  9 12 15 18 21
#  4 |  0  4  8 12 16 20 24 28
#  5 |  0  5 10 15 20 25 30 35
#  6 |  0  6 12 18 24 30 36 42
#  7 |  0  7 14 21 28 35 42 49
# Note. This is an exercise in for-loops and string formatting, see pyformat.info


n = 7 + 1

mat = []
for idx1 in range(n):
    mat.append([])
    for idx2 in range(n):
        mat[idx1].append(idx1 * idx2)

for row in mat:
    print(row)
