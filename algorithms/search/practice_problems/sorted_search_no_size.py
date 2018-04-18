
class Listy(list):
    def __init__(self, arr=None):
        if not arr:
            super().__init__()
        else:
            super().__init__(arr)

    def __len__(self):
        return None

    def __getitem__(self, key):
        """
        Overwrites normal array access so that leaf nodes return none instead of
        index errors
        Input:
            (int) = Index of the node to be returned
        Output:
            (object || None) = If there is a node at that index, that node value
                                will be returned. None if there is no node at index
        """
        try:
            return super().__getitem__(key)
        except IndexError:
            return -1

def listy_search(arr, value):

    if arr[0] == -1 or arr[0] > value:
        return False

    return list_up(arr, value, 0)

def list_up(arr, value, power=0, start=0):
    end = 2**power

    if arr[start] == -1:
        return False

    if arr[start] <= value and (arr[end] >= value or arr[end] == -1):
        return list_down(arr, value, start, end)

    if arr[end] < value:
        return list_up(arr, value, power + 1, end)

def list_down(arr, value, start=0, end=0):
    mid = (end + start) // 2
    if start > end:
        return False

    if arr[mid] == value:
        return mid
    elif arr[mid] > value or arr[mid] == -1:
        return list_down(arr, value, start, mid)
    elif arr[mid] < value:
        return list_down(arr, value, mid+1, end)
