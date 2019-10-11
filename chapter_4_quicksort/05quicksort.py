# quicksort is a faster sorting algorithm than selection sort
# Here are the steps:
# 1. Pick a Pivot
# 2. Partition the array into two sub-arrays: 
#    - elements less than the pivot and 
#    - elements greater than the pivot 
# 3. Call quicksort recursively on the two subarrays

def quicksort(array):
    if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
        return array
    else:
        # recursive case 
        pivot = array[0]
        # sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot 
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

    print(quicksort([10, 5, 2, 3]))


# D&C works by breaking a problen down into smaller and smaller pieces. 
# If youre using D&C on a list, the base case is problem an empty array or an array with one element.

# If you're implementing quicksort, choose a random element as the pivot. The average runtime of quicksort is O(nlogn)!
# The constant in Big O notation can sometimes matter. That's why quicksort is faster than merge sort 
# The constant almost never matters or simple search versus binary search, because O(logn) is so much faster than O(n) when your list gets big
