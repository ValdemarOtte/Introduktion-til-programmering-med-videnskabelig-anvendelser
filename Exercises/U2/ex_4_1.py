# NOTE : Opgavebeskrivelse
# Exercise 4.1 (list aliasing and list copy)
# Consider the below code. Run the code and explain the output.
# Hint. Try to use www.pythontutor.com.

a = [[1, 2], [3, 4]]
b = a
c = a[:]
b[0] = [5, 6]
c[1][1] = 7
print(a, b, c)