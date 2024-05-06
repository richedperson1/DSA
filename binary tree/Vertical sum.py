from binary_tree import createTree
from collections import defaultdict
class Solution:
    #Complete the function below
    def verticalSum(self, root):
        #:param root: root of the given tree.
        
        dist = defaultdict(int)
        def dfs(root,level):
            if not root:
                return             
            dist[level] += root.data
            dfs(root.left,level-1)
            dfs(root.right,level+1)
        
        dfs(root,0)
        dist = sorted(dist.items(),key = lambda x : x[0])
        # dist = sorted(dist)
        print(dist)
        result = []
        for data in dist:
            result.append(data[-1])
        return result
    


arr = list(map(int,"1 2 3 4 5 6 7".split()))
tree = createTree().createTreeUsingList(arr)

obj_sol = Solution()
print(obj_sol.verticalSum(tree))