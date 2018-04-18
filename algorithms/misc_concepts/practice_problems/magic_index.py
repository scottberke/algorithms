# O(log n) This is just binary search 
def magic_index(arr, start, end):
    if start >= end:
        return False

    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return magic_index(arr, mid + 1, end)
    else:
        return magic_index(arr, start, mid)
