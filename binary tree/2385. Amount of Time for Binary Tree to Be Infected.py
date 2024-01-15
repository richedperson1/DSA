from collections import deque
from binary_tree import createTree,root
def amountOfTime( root, start: int) -> int:
    
    root.adj = []
    root.adj.append(root.left)
    root.adj.append(root.right)
    def make_parent(root,parent):
        if not root:
            return root

        root.adj =[]
        root.adj.append(parent)
        if root.left:
            root.adj.append(root.left)
            make_parent(root.left,root)
        if root.right:
            root.adj.append(root.right)
            make_parent(root.right,root)


    make_parent(root.left,root)
    make_parent(root.right,root)

    def dfs(root):
        if not root:
            return -1
        if root.data== start:
            return root

        # if dfs(root.left):
        #     return dfs(root.left)
        right = dfs(root.right)
        if right!=-1:
            return right
        left = dfs(root.left)
        
        
        return left
        

    lead_role = dfs(root)
    print(lead_role)
    if lead_role==-1:
        return -1


    dq = deque([(lead_role,0)])
    time = 0
    visit = set([lead_role])
    while len(dq)>0:
        front_data,level = dq.popleft()
        time = level
        for data in front_data.adj:
            if data not in visit and data:
                dq.append([data,level+1])
                visit.add(data)
    return  time
    
binary_arr = [1]
k = 1
null = -1
tree_create = createTree().createTreeUsingList(arr)
print(tree_create)
print(amountOfTime(tree_create,k))
# root.print_tree(tree_create)