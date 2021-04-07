def merge(arr: list, left: int, mid: int, right: int):
    print(left, mid, right)
    left_copy = arr[left:mid]
    right_copy = arr[mid:right]
    print(left_copy, right_copy)
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
    print(arr)
    return arr


def merge_sort(arr: list, left: int, right: int):
    if left >= right:
        return
    mid = (right + left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)
    merge(arr, left, mid, right)


a = [0, 1, 0, 1, 4, 3]
merge_sort(a, 0, 4)