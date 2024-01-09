from collections import Counter
def canPair( nums, k):
    size = len(nums)
    if size&1:
        return False
    nums = [num%k for num in nums]
    dist = Counter(nums)
    # print(dist)
    for key,val in dist.items():
        
        divide = (key%k)
        if divide==0:
            if dist[divide]&1==0:
                dist[0]=0
                continue
            return False
            # dist[divide]-=2
            # continue
        remain =k-(key%k)
        if dist.get(key)<=0:
            continue
        
        if remain in dist :
            
            if dist.get(remain)<=0:
                return False
            else:
                dist[remain] -=1
                dist[key]-=1
        else:
            return False
    
    for val in dist.values():
        if val&1:
            return False
    return True


arr = [4,4,4,4,4,4]

print(canPair(arr,4))