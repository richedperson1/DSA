
seg = [0]


def buildingSeg(arr,ind,low,high):
    if low==high:
        size = 1+ind-len(seg)
        newArr = [0]*size
        seg.extend(newArr)
        seg[ind] = arr[low]
        return
    
    mid = (low+high)//2

    buildingSeg(arr,ind*2+1,low,mid)
    buildingSeg(arr,ind*2+2,mid+1,high)
    seg[ind] = max(seg[ind*2+1],seg[ind*2+2])

    # return 



def segmentTree(arr):
    low,high = 0,len(arr)-1
    buildingSeg(arr,0,low,high)

    print(seg)
    return seg


arr = [10,12,3,4]

print(segmentTree(arr))
    