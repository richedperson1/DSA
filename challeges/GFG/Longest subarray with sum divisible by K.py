
arr = [-1,-1,-1,-1,-1]

k = 2

def longest_subarray(arr,k):
    
    dist = {}
    total = 0
    result = 0
    for ind,data in enumerate(arr):
        total+=data
        res = total%k
        
        if res==0:
            result = max(result,ind+1)
        
        # if res<0:
        #     res += k
        if res in dist:
            result = max(result,ind-dist[res])
        else:
            dist[res] = ind
            
    return result
    
print(longest_subarray(arr,k))