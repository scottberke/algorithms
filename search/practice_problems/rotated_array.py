
# Basically binary search so O(log n)
def search_rotated_array(arr, low, high, target):
    if low > high:
        return False
    mid = (low + high) // 2
    if arr[mid] == target:
        return arr[mid]
    if arr[mid] < arr[high]: # right sides ordered
        if arr[mid] < target and arr[high] >= target:
            return search_rotated_array(arr, mid + 1, high, target)
        else:
            return search_rotated_array(arr, low, mid - 1, target)
    if arr[mid] > arr[high]: # right sides out of order
        if arr[low] <= target and arr[mid] > target:
            return search_rotated_array(arr, low, mid - 1, target)
        else:
            return search_rotated_array(arr, mid + 1, high, target)
