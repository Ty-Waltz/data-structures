def simple_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
# This code steps through the arr repeadedly, compares elements in the wrong order, amd sorts them until they are in the right order
# Outer Loop is responsible fo reducing the range of the elements being compared
# Inner Loop iterates n-i-1 for each iteration of the outer loop. This performs a comparison between adjacent elements
# Compares elements to determine order
# if True the elements are swapped
# This method can take time because it has to run through each adjacent element until they are all sorted

#Worst case: a swap occcurs for every comparison

#Best case: the array is already sorted, all comparisons are made, adn no swaps occure

# This code's strengths:
#   Simple to implement, works well for a small database, and its stable for sorting

# Weaknesses:
#   Inneficient if you wanted to scale up the database
#   Always performs every comparison

# To improve the effiency of the code, implement  a flag check  to see if swaps were made instead of checking every element for a swap
# If no swaps occur, then it breaks out of the loop as the arr is already in  the correct order
# Best case time complexity
def optimized_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
