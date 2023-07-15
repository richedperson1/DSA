# ! https://practice.geeksforgeeks.org/problems/flood-fill-algorithm1856/1
"""
Time complexity : O(n*m)
Space complexity : O(n)
"""

def floodFill( image, sr, sc, newColor):
    #Code here
    mainColor = image[sr][sc]
    # image[sr][sc] = newColor
    visit = set()
    def dfs(row,col):
        if row>=rows or col>=cols or row<0 or col<0:
            return 0
        
            
        if (row,col) in visit or image[row][col]!=mainColor:
            return 0
            
        local = [[-1,0],[1,0],[0,1],[0,-1]]
        visit.add((row,col))
        image[row][col] = newColor
        for r,c in local:
            newRow = row+r
            newCol = col+c
            if (newRow,newCol) not in visit :
                dfs(newRow,newCol)
        
    rows = len(image)
    cols = len(image[0])
    
    dfs(sr,sc)
    return image

"""
Time complexity : O(n*m)
Space complexity : O(1)
"""

def floodFill2( image, sr, sc, newColor):
    #Code here
    mainColor = image[sr][sc]
    # image[sr][sc] = newColor
    visit = set()
    def dfs(row,col):
        if row>=rows or col>=cols or row<0 or col<0:
            return 0
        
            
        if image[row][col]==newColor or image[row][col]!=mainColor:
            return 0
            
        local = [[-1,0],[1,0],[0,1],[0,-1]]

        image[row][col] = newColor
        for r,c in local:
            newRow = row+r
            newCol = col+c
            dfs(newRow,newCol)
        
    rows = len(image)
    cols = len(image[0])
    
    dfs(sr,sc)
    return image

element = '''0 0 1 0 1
1 1 0 1 0
0 0 1 1 0
0 0 1 1 0'''

grid = [list(map(int,data.split())) for data in element.split('\n')]
grid = [[1,1,1],[1,1,0],[1,0,1]]

# ( image, sr, sc, newColor)
print(floodFill2(grid,1,1,2))
