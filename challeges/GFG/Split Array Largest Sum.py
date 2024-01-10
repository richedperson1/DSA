def splitArray( arr,  k):
    # code here 
    
    def check_data(mid,k):
        total = 0
        t_k = 1
        for data in arr:
            if data>mid:
                return False
            if total+data<=mid:
                total+=data
            else:
                total = data
                t_k+=1
        if t_k>=k:
            return True
        return False
    
    low,high = min(arr),sum(arr)
    
    ans = float("inf")
    while low<=high:
        
        mid = (low+high)//2
        
        if check_data(mid,k):
            ans = min(ans,mid)
            high = mid-1
        else:
            low = mid+1
    return ans if ans<float("inf") else -1

arr = [1,2,3,4]
k = 1
print(splitArray(arr,k))