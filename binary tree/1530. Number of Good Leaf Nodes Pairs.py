from binary_tree import *
class Solution:
    def countPairs(self, root: root, dist: int) -> int:

        self.total = 0
        self.dfs(root,dist)
        return self.total

    def dfs(self,root,dist):
        if not root:
            return 0
        
        if root.left==None and root.right==None:
            return [1,1]

        left = self.dfs(root.left,dist)
        right= self.dfs(root.right,dist)


        if isinstance(left,list) and isinstance(right,list) :
            if  left[1]+right[1]<=dist:
                self.total+= (right[0]+left[0])//2
            return [(right[0]+left[0])//2,left[1]+right[1]]
        
        elif  isinstance(left,list) or isinstance(right,list):
            ans =  left or right
            ans[1]+=1
            return ans
        
        return 0
    
    
arr = [1,2,3,4,5,6,7]
arr =[7,1,4,6,-1,5,3,-1,-1,-1,-1,-1,2]
dist = 3
treeNode = createTree().createTreeUsingList(arr)


print(Solution().countPairs(treeNode,dist))