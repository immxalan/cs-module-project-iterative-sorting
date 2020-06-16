def linear_search(arr, target):
    # Your code here
    for index, value in enumerate(arr):
        if value == target:
            return index

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    top = len(arr) - 1
    bottom = 0
    while bottom <= top:
        mid = (top + bottom) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            bottom = mid + 1
        elif arr[mid] > target:
            top = mid - 1

    return -1  # not found
