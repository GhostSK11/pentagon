""" Julius Pazitka 
Project Euler Problem 15 
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner. How many such routes are there through a 20×20 grid? """

import math as m # in this solution, we use a standard math library (We need this library, for working with mathematical formula)
# as m 
# We use math as m to give a library a short alias while importing it.

a = 20 # represent 20x20 grid 
result = m.factorial(2*a)//(m.factorial(a)**2) # formula  
print("There are", result, "routes in 20x20 grid.") 
""" To compute the solution, we use binomial distribution. 
We think, that is the easiest way."""
input("Press any key")

# The result is 137846528820
# https://github.com/nayuki/Project-Euler-solutions/blob/master/Answers.txt (just for control)