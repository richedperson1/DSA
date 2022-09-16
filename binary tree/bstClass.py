from binary_tree import *


class BST:
    def __init__(self, rootNode=None):
        self.rootNode = rootNode
        self.numNode = 0

    def printHelper(self, rootNode):
        if rootNode == None:

            return
        print(rootNode.data, end=" :--> ")
        if rootNode.left:
            print("L :", rootNode.left.data, " ", end=" ")
        if rootNode.right:
            print("R :", rootNode.right.data, end="  ")
        print()
        self.printHelper(rootNode=rootNode.left)
        self.printHelper(rootNode=rootNode.right)

    def printTree(self):
        return self.printHelper(self.rootNode)

    def isPresent(self, k):
        if self.rootNode == None:
            return -1
        elif self.rootNode.data == k:
            return self.rootNode

        elif self.rootNode.data > k:
            return self.checkElementInTree(self.rootNode.left, k)
        else:
            return self.checkElementInTree(self.rootNode.right, k)

    def checkElementInTree(self, rootNode, k):
        if rootNode == None:
            return -1
        elif rootNode.data == k:
            return rootNode

        elif rootNode.data > k:
            left = self.checkElementInTree(rootNode=rootNode.left, k=k)
            return left

        else:
            rgt = self.checkElementInTree(rootNode.right, k)
            return rgt

    def insertElements(self, ele):
        self.numNode += 1
        self.rootNode = self.insertHelper(self.rootNode, ele)

    def insertHelper(self, rootNode, ele):
        if rootNode == None:

            return root(ele)

        if rootNode.data > ele:
            rootNode.left = self.insertHelper(rootNode.left, ele)
            return rootNode
        else:
            rootNode.right = self.insertHelper(rootNode.right, ele)
            return rootNode

    def deleteNode(self, data):
        isDel, rootNode1 = self.deleteHelper(self.rootNode, data)
        if isDel:
            self.numNode -= 1
            self.rootNode = rootNode1
        return isDel, rootNode1

    def deleteHelper(self, nodes, data):
        if nodes == None:
            return False, nodes
        if nodes.data > data:
            isDel, rootNode = self.deleteHelper(nodes.left, data)
            nodes.left = rootNode
            return isDel, nodes
        if nodes.data < data:
            isDel, rootNode = self.deleteHelper(nodes.right, data)
            nodes.right = rootNode
            return isDel, nodes
        # When zero child present
        if nodes.left == None and nodes.right == None:
            return True, None

        # when nodes has right child
        if nodes.right and not(nodes.left):
            return True, nodes.right

        # When nodes has left child
        if nodes.left and not(nodes.right):

            return True, nodes.left

        # When nodes has 2 childs
        if nodes.left and nodes.right:
            replacement = self.min(nodes.right)
            nodes.data = replacement
            # print(replacement)
            isDel, newNodes = self.deleteHelper(nodes.right, replacement)
            nodes.right = newNodes
            return isDel, nodes

    def min(self, repel):
        if repel == None:
            return 100000
        if repel.left == None:
            return repel.data
        return self.min(repel.left)


lst = [5, 3, 10, 1, 4, 7, 15, 0, 2, 3.5, 4.5]
bstTree = createTree().createTreeUsingList(lst)
duplicate = cloning().cloneWholeTree(bstTree)
treeObj = BST(duplicate)
Bool, tree = treeObj.deleteNode(3)
root.print_tree(tree)
