# NOTE : Opgavebeskrivelse
# Exercise 4.2 (infinite recursive list)
# Run the below code and explain what is happing.

a = [42]
a[0] = a    # Der bliver ændret i det første index i listen a 
print(a)    # Nu bliver det til en list i en list, da a er en liste