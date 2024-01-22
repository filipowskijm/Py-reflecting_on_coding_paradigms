## Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

# How does this solution ensure data immutability?
# It doesn't modify the data, only sorts it

# Is this solution a pure function? Why or why not?\
# Yes, it only returns the values that were inputted, just in a different order

# Is this solution a higher order function? Why or why not?
# Yes, it uses another function inside of the function, append

# Would it have been easier to solve this problem using a different programming style?
# Most likely, yes 

# Why in particular is functional programming a helpful paradigm when solving this problem?
# It is easier to understand and more resistant to bugs