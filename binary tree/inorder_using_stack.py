class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(noode):
            if not noode:
                return noode

            curr = noode
            stack = []

            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr = curr.left

                curr = stack.pop()
                ans.append(curr.val)
                curr = curr.right                    

        inorder(root)
        return ans