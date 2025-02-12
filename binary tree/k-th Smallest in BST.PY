"""
GFG link : https://www.geeksforgeeks.org/problems/find-k-th-smallest-element-in-bst/1

"""
class Solution:
    """
    This code snippet defines a method `kthSmallest` inside a class `Solution` that finds the k-th smallest element in a Binary Search Tree (BST).
    
    Time Complexity : O(n)
    Space Complexity : O(1)
    """
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        
        self.count = 0
        self.ele = -1
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            self.count+=1
            if self.count==k:
                self.ele = root.data
            
            dfs(root.right)
        
        dfs(root)
        return self.ele