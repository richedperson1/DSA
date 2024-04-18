def twoRepeated( arr , n):
    #Your code here
    ans = []
    for ind,data in enumerate(arr):
        local = abs(data)-1
        
        if arr[local]<0:
            ans.append(abs(data))
        else:
            arr[local] = -arr[local]
    return ans


arr = list(map(int,"2 1 3 2 1".split()))
n = len(arr)
print(twoRepeated(arr,n))
