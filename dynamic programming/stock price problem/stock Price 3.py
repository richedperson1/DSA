arr = [3, 2, 6, 5, 0, 3]


def stockPrice3(ind, flag, k):
    if len(arr) <= ind or k < 0:
        return 0

    if flag:
        kharido = -arr[ind]+stockPrice3(ind+1, 0, k-1)
        chupKaro = stockPrice3(ind+1, 1, k)
        return max(kharido, chupKaro)

    else:
        kharido = arr[ind]+stockPrice3(ind+1, 1, k)
        chupKaro = stockPrice3(ind+1, 0, k)
        return max(kharido, chupKaro)


print(stockPrice3(0, 1, 2))
