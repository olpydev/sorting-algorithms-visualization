def merge_sort(array, left, right):
    if left < right:
        mid = (left + right) // 2
        yield from merge_sort(array, left, mid)
        yield from merge_sort(array, mid+1, right)
        yield from merge(array, left, mid, right)


def merge(array, left, mid, right):
    L = array[left:mid+1]
    R = array[mid+1:right+1]
    i = 0
    j = 0
    k = left
    while i < len(L) and j < len(R):
        yield array, left+i, mid+j, left, right
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        array[k] = R[j]
        j += 1
        k += 1
