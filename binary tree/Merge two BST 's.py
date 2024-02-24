from binary_tree import *

class Solution:

    def merge(self, root1, root2):
        #code here.
        ans1 = []
        def dfs(root,ans):
            if not root:
                return
            
            dfs(root.left,ans)
            ans.append(root.data)
            dfs(root.right,ans)
        
        dfs(root1,ans1)
        ans2 = []
        dfs(root2,ans2)
        print(ans1)
        print(ans2)
        n1,n2 = len(ans1),len(ans2)
        final = []
        i,j = 0,0
        while i<n1 and j<n2:
            if ans1[i]>ans2[j]:
                final.append(ans2[j])
                j+=1
            else:
                final.append(ans1[i])
                i+=1
        while i<n1:
            final.append(ans1[i])
            i+=1
            
        while j<n2:
            final.append(ans1[j])
            j+=1
        
        return final
    

arr = list(map(int,"5 3 6 2 4".split()))
brr = list(map(int,"2 1 3 -1 -1 -1 7 6".split()))
arr.extend([-1]*10)
brr.extend([-1]*5)

t2 = createTree().createTreeUsingList(arr)
t1 = createTree().createTreeUsingList(brr)

obj = Solution()

print(obj.merge(t1,t2))