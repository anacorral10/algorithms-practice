# The sum function should work like this:
# 1. given an list of numbers: 
# 2. if the list is empty, return zero
# 3. otherwise the total sum is the first number in the list + the sum of the rest of the list 

# remember recursion helps keep track of the state

def sum(list):
    if list == []:
        return 0 
    return list[0] + sum(list[1:])
