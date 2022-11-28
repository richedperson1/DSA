# Function to reverse every sub-array group of size k.
def reverseInGroups(arr, N, k):
    i = 0
    while i+k <= N:
        start = i
        end = i+k-1
        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        i += k

    if i+k > N:
        start = i
        end = N-1
        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    return arr


arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 3
print(reverseInGroups(arr, n, k))
print(arr)
