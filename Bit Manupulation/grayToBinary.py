
class Solution:    
    ##Complete this function
    # function to convert a given Gray equivalent n to Binary equivalent.
    def grayToBinary(self,n):
        ##Your code here
        binc=""
        for i in range(31,-1,-1):
            k=n>>i
            if(k&1):
                binc+='1'
            else:
                binc+='0'
        res=binc[0]
        print(binc)
        for i in range(1,len(binc)):
            res+=str(int(res[i-1])^int(binc[i]))
        return int(res,2)
    

n = 4
obj = Solution().grayToBinary(n)