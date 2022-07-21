
arr = [0, 1, 0, 2, 1, 0, 1, 0, 2, 1, 0, 1, 0, 1, 2, 2]


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


low = 0
high = len(arr)-1
mid = 0
i = 0
while mid<=high:
    if arr[mid] == 0:
        swap(arr, low, mid)
        low += 1
        mid += 1
    elif arr[i] ==1:
        mid+=1
    else:
        pass 