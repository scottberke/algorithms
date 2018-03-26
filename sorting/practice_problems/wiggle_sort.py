# O(n)
def wiggle_sort(arr):
    for i in range(len(arr)-1):
        if is_even(i) and arr[i] > arr[i+1]:
            swap(i, i+1, arr)
        elif not is_even(i) and  arr[i] < arr[i+1]:
            swap(i, i+1, arr)
    return arr

def swap(index_1, index_2, arr):
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]

def is_even(index):
    return index%2 == 0
