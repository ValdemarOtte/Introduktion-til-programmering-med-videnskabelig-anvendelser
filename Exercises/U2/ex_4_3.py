# NOTE : Opgavebeskrivelse
# Exercise 4.3 (infinite recursive indexing)
# Run the below code and explain what is happing.

x = [0, 7]
x[0] = x
print(x)
print(x[1])
print(x[0][1])
print(x[0][0][1])
print(x[0][0][0][1])
print(x[0][0][0][0][1])
print(x[0][0][0][0][0][1])
