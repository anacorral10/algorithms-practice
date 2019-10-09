# Write a function that prints a countdown
# => 3..2..1

# Every Recursive function has two parts: 
# 1. Base case: When the function doesn't call itself again..so it doesn't go on an infinite loop
# 2. Recursive case: When the function calls itself


def countdown(i):
    # base case
    if i <= 0:
        return 0 
    #recusive case
    else:
        print(i)
        return countdown(i-1)

countdown(5)

