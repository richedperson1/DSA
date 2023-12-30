def removeKdigits( num: str, k: int) -> str:
    size = len(num)
    ans = int(num)
    def helper(num,k):
        size = len(num)
        nonlocal ans
        if size<=0:
            ans = 0
            return 0
        if k==0:
            if int(num)<=0:
                ans = 0
                return 0
            ans = min(ans,int(num))
            return ans
        
        for ind in range(size):
            helper(num[:ind]+num[ind+1:],k-1)
            pass
        return ans
    
    
    print(helper(num,k))
    return ans


num = "18199999"
print(removeKdigits(num,3))