def merge(arr: list, left: int, mid: int, right: int):
    left_copy = arr[left:mid + 1]
    right_copy = arr[mid + 1:right + 1]
    i, j = 0, 0
    sorted_idx = left
    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            arr[sorted_idx] = left_copy[i]
            i += 1
        else:
            arr[sorted_idx] = right_copy[j]
            j += 1
        sorted_idx += 1
    while i < len(left_copy):
        arr[sorted_idx] = left_copy[i]
        sorted_idx += 1
        i += 1
    while j < len(right_copy):
        arr[sorted_idx] = right_copy[j]
        sorted_idx += 1
        j += 1
    return arr


def merge_sort(arr: list, left: int, right: int):
    if left >= right:
        return
    mid = (right + left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid+1, right)
    merge(arr, left, mid, right)


array = [1, 0]
merge_sort(array, 0, len(array) - 1)
print(array)


