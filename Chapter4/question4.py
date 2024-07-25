def mystery(x):
 y = 0
 for value in x:
     y += value ** 2
 return y
print(mystery([1, 2, 3, 4, 5]))


##it iterates over the list provided in the arugment in place of the parameter and while iterating over each value provides the square of each value.
