# Problem: Sort an array from smallest to largest

# First create a Function that finds the smallest element in an array
def findSmallest(arr):
    # Stores the smallest value
    smallest = arr[0]
    # Stores the index of the smallest value
    smallest_index = 0 
    for i in range(1, len(arr)):
        if arr[i] <  smallest:
            smallest_index = i 
            smallest = arr[i]
        return smallest_index

# Now you can use this function to write selection sort:
# Sorts an Array
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # Finds the smallest element in the array and adds it to the new array
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))

## Selection Sort is a neat algorithm but it's not very fast. Quicksort is a faster sorting algorithm