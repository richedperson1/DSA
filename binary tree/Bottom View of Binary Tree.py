class Solution:
    def bottomView(self, root):
        # code here
        dist = {}
        dq = deque([(root,0)])
        ans = []
        while len(dq)>0:
            root,level = dq.popleft()
            
            dist[level] = root.data
            
            if root and root.left :
                dq.append((root.left,level-1))
            
            if root and root.right:
                dq.append((root.right,level+1))

        for data in sorted(dist):
            ans.append(dist[data])
        return ans