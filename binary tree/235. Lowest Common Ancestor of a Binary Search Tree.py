from binary_tree import *

class Solution:
    def lowestCommonAncestor(self, root, p, q) :
        ans = set([])
        ans1 = set([])
        def dfs(root,tar,ans):
            if not root:
                return

            left = dfs(root.left,tar,ans)
            right= dfs(root.right,tar,ans)
            if left or right:
                ans.add(root)
                return True
            if root.val==tar:
                return True
            return False
        dfs(root,p,ans)
        dfs(root,q,ans1)
        z = ans.intersection(ans1)
        print(ans,ans1,z)
        return root
    
null = -1
arr = [6,2,8,0,4,7,9,null,null,3,5]
p = 2
q = 4
tree = createTree().createTreeUsingList(arr)
obj = Solution()
obj.lowestCommonAncestor(tree,p,q)