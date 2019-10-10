# write a recursive function to count the number of items in a list 

def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])