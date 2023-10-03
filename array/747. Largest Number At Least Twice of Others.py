def dominantIndex( arr: list[int]) -> int:
    
    prev = None
    first,second = -1,-1
    size = len(arr)
    ind = 0
    for i in range(size):
        if (arr[i] > first):
            second = first
            first = arr[i]
            ind = i

        elif (arr[i] > second and arr[i] != first):
            second = arr[i]
    
    print(first,second)
    if(second*2<=first):
        return 1
    return -1


arr = [3,6,1,0]
print(dominantIndex(arr))