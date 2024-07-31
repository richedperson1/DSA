class Solution:
    def rowWithMax1s(self,arr):
        result = 0
        res_ind= -1
        
        for ind, data in enumerate(arr):
            
            if data[0]==data[-1] and data[0]!=0:
                return ind
            
            local = sum(data)
            
            if local>result:
                result = local
                res_ind = ind
                
        return res_ind
                
                
            
arr = [[0, 0, 0], [0, 0, 1]]
obj = Solution()

print(obj.rowWithMax1s(arr))