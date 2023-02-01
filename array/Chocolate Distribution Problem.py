

def distribution(arr, m, n):
    arr = sorted(arr)
    diff = arr[0]
    final = arr[m-1]

    diff = final-diff
    start = 1
    local = 0
    for ind in range(m, n):

        local = arr[ind] - arr[start]
        start += 1
        diff = min(diff, local)
    return diff


N = 8
M = 5
A = [3, 4, 1, 9, 56, 7, 9, 1, 1, 12]

print(distribution(A, M, N))
