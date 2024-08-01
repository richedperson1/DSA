class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        
        arr = []
        
        def dfs(srow,erow,scol,ecol):
            if (srow>erow or scol>ecol) or (srow==erow and scol==ecol):
                return
            
            for col in range(scol,ecol+1):
                arr.append(mat[srow][col])
                
            srow+=1
            
            for row in range(srow,erow+1):
                arr.append(mat[row][ecol])
                
            ecol-=1
            
            for col in range(ecol,scol-1,-1):
                arr.append(mat[erow][col])
                
            erow-=1
            
            for row in range(erow,scol,-1):
                arr.append(mat[row][scol])
                
            scol+=1
            
            dfs(srow,erow,scol,ecol)
        
        rows,cols = len(mat),len(mat[0])
        dfs(0,rows-1,0,cols-1)
        return arr
    
obj = Solution()

mat = [[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12]]

print(obj.spirallyTraverse(mat))