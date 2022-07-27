arr = [1, 2, 3]
n = len(arr)

# Methods 1


def majorityElement(arr, n):
    # Your code here
    if n == 1:
        return(arr[0])
        # ()
    arr = sorted(arr)

    i = 0
    count = 1
    maxi = 0
    num = arr[0]
    while i < n:
        while i < n-1 and arr[i] == arr[i+1]:
            count += 1
            i += 1
        if count > maxi:
            maxi = count
            num = arr[i]

        count = 1
        i += 1
    if maxi > int(n/2):
        return(num)
    else:
        return -1

# Methods 2


# using space O(n)
arr = [1, 2, 2, 2]
n = len(arr)


def major(arr, n):
    dist = {}
    count = 1
    num = arr[0]
    for num in arr:
        if num in dist:
            dist[num] += 1
            if count < dist[num]:
                count = dist[num]
                num = num
        else:
            dist[num] = 1
    # for key, val in dist.items():
    #     if val > count:
    #         num = key
    #         count = val
    if count > (n/2):
        return num, count
    else:
        return -1


print(major(arr, n))
