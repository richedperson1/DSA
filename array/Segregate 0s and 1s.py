arr = [0,0,1,1,0]
arr = list(map(int,"1 0 0 1 0 0 0 0 0 1 1 1 1 1 1 1 0 1 0 1 0 0 1 0 0 1 0 0 1 1 0 1 0 1 0 1 1 1 0 1 1 0".split()))
end = len(arr)-1
low ,high = 0,end
for ind in range(len(arr)):
    if arr[ind]==0:
        arr[ind],arr[low] = arr[low],arr[ind]
        low+=1


print(arr)

