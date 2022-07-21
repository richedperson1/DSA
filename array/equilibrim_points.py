# arr = [1, 1]


def naive_sol(arr, n):
    # n = len(arr)
    if n <= 1:
        return(1)
    if n == 2:
        return -1

    for i in range(1, n):
        local1 = 0
        for j in range(i-1, -1, -1):
            local1 += arr[j]
        local2 = 0
        for j in range(i+1, n):
            local2 += arr[j]
        if local1 == local2:
            return i+1
    return -1


def better_solution(arr, n):

    ans = [0]*n
    total = 0
    for i in range(n-1, -1, -1):
        total += arr[i]
        ans[i] += total

    local1 = arr[0]
    for j in range(1, n):
        check = ans[j]-arr[j]
        if check == local1:
            return j+1
        local1 += arr[j]

    return -1


def optimize_solution(arr, n):
    total = sum(arr)
    n = len(arr)
    if n <= 1:
        return(1)
    prefix = arr[0]
    for i in range(1, n):
        local = total-prefix-arr[i]
        if local == prefix:
            return(i+1)
        prefix += arr[i]
    return(-1)


arr = [0, 100, 6, 100, 0]
n = len(arr)
print(naive_sol(arr, n))
print(better_solution(arr, n))
print(optimize_solution(arr, n))