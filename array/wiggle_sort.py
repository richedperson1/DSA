def wiggleSort(arr):
    arr1 = sorted(arr)
    print(arr1)
    size = len(arr)
    ind = 0
    while ind<size:
        arr[ind] = arr1[ind]
        if ind+1<size:
            arr[ind+1] = arr1[-(ind+1)]
        ind+=2
    return arr

ans = [3,5,2,1,6,4]
print(wiggleSort(ans))