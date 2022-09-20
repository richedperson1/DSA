import queue


class tree:
    def __init__(self, data=None):
        self.data = data
        self.nodes = list()

    @staticmethod
    def printGTree(root):
        # This is not base case but it's edge case where if root is None when input is given then don't error
        if root == None:
            return

        print(root.data, end=" : ")
        for idx, child in enumerate(root.nodes):
            if idx+1 == len(root.nodes):
                print(child.data, end="")
            else:
                print(child.data, end=" , ")
        print()
        for i in range(len(root.nodes)):
            tree.printGTree(root.nodes[i])


class createTree:
    def createTreeFromInput(self, lst, rootHead=None):
        ind = 0
        if rootHead:
            rootNode = rootHead
            pass
        else:
            rootNode = tree(lst[0])
            ind += 1

        pastNode = queue.Queue()
        pastNode.put(rootNode)

        while not(pastNode.empty()) and ind < len(lst):
            curr = pastNode.get()
            while ind < len(lst) and lst[ind] != -1:
                new = tree(lst[ind])
                ind += 1
                curr.nodes.append(new)
                pastNode.put(new)
            ind += 1
        return rootNode
