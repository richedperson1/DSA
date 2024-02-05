from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        stack = deque([(root,(0,0))])

        ans = []
        while len(stack)>0:
            root,level = stack.popleft()
            col,row = level

            ans.append((col,row,root.val))
            if root and root.right:
                stack.append((root.right,(col+1,row+1)))

            if root and root.left:
                stack.append((root.left,(col-1,row+1)))

        ans = sorted(ans)

        # print(ans)
        new_result = []
        prev = None
        for data in ans:
            col,row,result = data
            if prev==col:
                new_result[-1].append(result)
                prev = col
            else:
                new_result.append([result])
                prev = col
        return new_result
    
