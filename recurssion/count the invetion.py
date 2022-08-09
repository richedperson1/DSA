def divide_2(arr, total):
    if len(arr) <= 1:
        return total
    mid = len(arr)//2
    right = arr[mid:]
    left = arr[0:mid]
    divide_2(right, total)
    divide_2(left, total)
    l = 0
    r = 0
    i = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            arr[i] = left[l]
            i += 1
            l += 1
        else:
            total += mid-l
            arr[i] = right[r]
            i += 1
            r += 1
    while l < len(left):
        arr[i] = left[l]
        l += 1
        i += 1
    while r < len(right):
        arr[i] = right[r]
        i += 1
        r += 1
    return total


def mergesort(arr, count):
    if len(arr) > 1:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        count = mergesort(l, count)
        count = mergesort(r, count)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                k += 1
                i += 1
            else:
                arr[k] = r[j]
                count = (count+len(l)-i)
                k += 1
                j += 1
        while i < len(l):
            arr[k] = l[i]
            k += 1
            i += 1
        while j < len(r):
            arr[k] = r[j]
            k += 1
            j += 1
        return count
    else:
        return count


arr = [5, 4, 3, 2, 1]
total = 0

print(divide_2(arr,  total))
print(mergesort(arr, total))
