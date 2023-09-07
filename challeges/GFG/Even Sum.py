"""
URL : https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-118/problems
"""



def EvenSum(arr):
    sumi = sum(arr)
    
    if sumi&1==0:
        return 0
    
    dist = []
    for ind,data in enumerate(arr):
        if data&1==0:
            dist.append(data)

    count = 0
    prev = None
    sumi = sum(arr)
    count = float("inf")
    
    for ind,data in enumerate(dist):
        local = 0
        while data&1==0:
            data = data//2
            local += 1
            
        count = min(local,count)
    return count

            
arr = [1, 2, 1, 2, 1]
arr = [1,1,1]
arr = [1,16,16,16,16]
print(EvenSum(arr))
        