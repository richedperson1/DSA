class Solution:
    def isWordExist(self, mat, word):
        rows = len(mat)
        cols = len(mat[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col, index):
            if index == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if mat[row][col] != word[index]:
                return False

            temp = mat[row][col]
            mat[row][col] = "*"
            for dr,dc in directions:
                new_row = row+dr
                new_col = col+dc
                
                if dfs(new_row,new_col,index+1):
                    return True
            
            mat[row][col] = temp
            
            return False
    
        for row in range(rows):
            for col in range(cols):
                if dfs(row,col,0):
                    return True
        return False


    
	            