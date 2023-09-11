

def maximumBeauty(k,arr):
    n = len(arr)
    dp = [[[float("inf")]*2 for ind in range(k+1)] for ind in range(n)]


def maximumBeauty2(k,arr):
    n = len(arr)
    dp = {}


    def beuti(count,ind):
        
        if count>=k:
            return 0
            
        if ind>=n:
            return float("-inf")

        if (count,ind) in dp :
            return dp[(count,ind)]
        
        pick = beuti(count,ind+1)
        noPick = beuti(count+1,ind+2)+arr[ind]
        ans = max(pick,noPick)
        dp[(count,ind)]= ans
        
        return ans


    return beuti(0,0)


# arr = [1,2,4,3,2,6]
# k = 2

arr = [1,10000000000000,1]
k = 2

print(maximumBeauty2(k,arr))
