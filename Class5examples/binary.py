#long code for searching binary algorithm
def binary_search(arr, target,left, right):
    #basecase: element not found
    if left > right:
        return -1
    mid = (left + right) // 2
    #basecase: element found
    if arr[mid] == target:
        return mid
    #recursive case
    elif arr[mid] <= target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)
    
sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(sorted_arr, target, 0, len(sorted_arr) - 1)
