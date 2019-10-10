# Divide & Conquer (D&C) 
# 1. figure out a simple case as the base case
# 2. figure out how to reduce your problem and get to the base case

# you're given an array of numbers.
# you have to add up all the numbers and return the total 
def sum(arr):
    total = 0
    for x in arr:
        total += x
        return total 

print sum([1, 2, 3, 4])

# but how do we do this for a recursive function?...