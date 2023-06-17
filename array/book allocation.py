def findPages(A, N, M):
    #code here
    def check(mid,m):
        
        total = 0
        for ind,data in enumerate(A):
            if total+data>=mid:
                m-=1
                total = 0
            total+=data

        return m<=0
    
    
    low = 0
    high= N-1
    ans = 0
    sumi = 0
    while low<high:
        mid = (low+high)//2
        
        sumi = sum(A[0:mid+1])
        
        if check(sumi,M):
            low = mid+1
            
            ans = sumi
            
        else:
            high = mid
    
    return ans


arr  = [12,34,67,90]
m = 3
n = len(arr)


print(findPages(arr,n,m))