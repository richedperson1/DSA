def toggle( n : int, arr : list[int]) -> int:
    
    indexZero = []
    prev = False
    for ind,data in enumerate(arr):
        if data==0 and prev==False:
            indexZero.append(ind)
            prev = True
        elif data==1:
            prev = False
    
    if len(indexZero)==0:
        return n
        
    ans = 0
    for ind in indexZero:
        local = 0
        ind21 = ind
        while ind21<n and arr[ind21]==0:
            local+=1
            ind21+=1
        
        ind2 = ind-1
        while ind2>=0 and arr[ind2]==1:
            local+=1
            ind2-=1
            
        ind2 = ind21
        while ind2< n and arr[ind2]==1:
            ind2+=1
            local+=1
            
        ans = max(local,ans)
    return ans


arr = [1,0,0,0,1]
n = len(arr)
print(toggle(n,arr))