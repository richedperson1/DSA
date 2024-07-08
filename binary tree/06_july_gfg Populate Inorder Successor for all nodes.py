from binary_tree import createTree,root
class root(root):

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None


class Solution:
    def populateNext(self, node):
        self.inorder_list = []
        def inorder(node):
            if not node:
                return node
            inorder(node.left)
            self.inorder_list.append(node)
            inorder(node.right)
        inorder(node)
        
        prev = root(-1)
        print(prev.__dict__)
        while len(self.inorder_list)>0:
            
            last_ele = self.inorder_list.pop()
            last_ele.next = prev
            prev = last_ele
        return node
class Solution:
    def populateNext(self, root):
        self.previous = None
        def inorder(node):
            if not node:
                return node
            inorder(node.left)
            if self.previous!=None:
                node.next = self.previous

            self.previous = node
            inorder(node.right)
        
        inorder(root)
        return root
    
arr = list(map(int,"10 8 12 3".split()))
arr.extend([-1]*5)

treeRoot = createTree().createTreeUsingList(arr)


root.print_tree(treeRoot)

obj = Solution()
print(obj.populateNext(treeRoot))