from math import ceil
def checkInvetion(arr):

    totalAns = 0

    def inversionCount(arr):
        nonlocal totalAns
        if len(arr)<=1:
            return totalAns

        size = len(arr)
        mid = ceil(size/2)

        left  = arr[:mid]
        right = arr[mid:]
        inversionCount(left)
        inversionCount(right)

        numI = len(left)
        numJ = len(right)
        i ,j,k = 0,0,0
        
        while i<numI and j<numJ:
            if left[i]>2*right[j]:
                totalAns+=(numI-i)
            a = 0
            if left[i]>right[j]:
                arr[k] = right[j]
                j+=1
            else:
                arr[k] = left[i]
                i+=1
            k+=1
        
        while i<numI:
            arr[k] = left[i]
            i+=1
            k+=1

        while j<numJ:
            arr[k] = right[j]
            j+=1
            k+=1

        return totalAns
    return  inversionCount(arr)  



arr = [2,4,3,5,1]

print(checkInvetion(arr))