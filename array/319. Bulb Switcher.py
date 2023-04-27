num = 9


def buldSwitcher(num):
    arr = [True]*(num+1)
    arr[0] = not arr[0]
    for ind in range(1, num+1):
        if ind == 1:

            continue
        else:
            local = ind
            while local < (num+1):
                arr[local] = not arr[local]
                local += ind

    return(sum(arr))


print(buldSwitcher(num))
