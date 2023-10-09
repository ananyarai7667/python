def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(f"The sorted array is: {arr}")

#If an error occurs during the execution of the code (e.g., if the file does not exist
# or if there is a permission issue), the original content of the file will be lost because 
# we're overwriting it unconditionally in the with open(filename, 'w') as file block.
# To avoid this issue, you can make use of a temporary variable to store the uppercase 
# content and write it to the file only if no exceptions occur.