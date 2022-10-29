
# with simple recursion solution
count = 0

n = 10


def feboSimple(n):
    global count
    count += 1
    if n <= 2:
        return 1
    return feboSimple(n-1)+feboSimple(n-2)


print("\nWith simple solution following is answer ")
print(f"{n}th febo series is : ", feboSimple(10))
print("Number of recursion call is : ", count)
print()
print("--"*20)
# with DP solution
count1 = 0


def feboDP(n):
    global count1
    count1 += 1
    if n <= 2:
        return 1

    if arr[n] != 0:
        return arr[n]

    arr[n] = feboDP(n-1)+feboDP(n-2)
    return arr[n]


arr = [0]*(n+1)
print("\nWith DP solution following is answer ")
print(f"{n}th febo series is : ", feboDP(n))
print("Number of recursion call is : ", count1)
