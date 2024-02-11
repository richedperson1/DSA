
from binary_tree import *

"""
The function `maxProduct` calculates the maximum product of the sums of two disjoint subtrees in a
binary tree.

:param root: The parameter "root" is the root node of a binary tree
:return: The function `maxProduct` returns an integer, which represents the maximum product of two
subtrees in the given binary tree.
"""
def maxProduct( root) -> int:

    dist = {}
    def total_count(root):
        if not root:
            return 0

        left = total_count(root.left)
        right= total_count(root.right)
        dist[root] = left+right+root.val
        return left+right+root.val
    
    total_sum = total_count(root)
    
    result = 0
    for key,val in dist.items():
        first = total_sum-val
        result = max(result,first*val)
    return(result)
        
    


arr = [1,2,3,4,5,6,-1]
tree = createTree().createTreeUsingList(arr)
print(maxProduct(tree))
# root.print_tree(tree)