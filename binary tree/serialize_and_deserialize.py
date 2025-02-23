
"""
Link : https://www.geeksforgeeks.org/problems/serialize-and-deserialize-a-binary-tree/1

Time complexity : O(n)
spae complexity : O(n)
"""

from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        arr = []
        
        dq = deque([root])
        
        while len(dq):
            node = dq.popleft()
            if node:
                arr.append(node.data)
                dq.append(node.left)
                dq.append(node.right)
            else:
                arr.append(None)
        return arr

    def deSerialize(self, arr):
        #code here
        if not arr or len(arr)==0:
            return arr
        token = arr.pop(0)
        head = Node(token)
        size = len(arr)
        dq = deque([head])
        ind = 0
        while  len(dq)>0 and ind<size:
            
            parent = dq.popleft()
            
            leftV = arr[ind]
            ind+=1
            if leftV:
                leftN = Node(leftV)
                parent.left = leftN
                dq.append(leftN)
            
            rightV = arr[ind]
            ind+=1            
            if rightV:
                rightN = Node(rightV)
                parent.right = rightN
                dq.append(rightN)
        return head
        
        
 