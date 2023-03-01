"""
URL : https://leetcode.com/problems/find-duplicate-subtrees/description/
"""
from collections import defaultdict
visit = defaultdict(str)
ans = []


def duplicateFind(root):
    if not root:
        return "Not"

    left = duplicateFind(root.left)
    right = duplicateFind(root.right)
    final = str(root.val)+","+left+right
    if len(visit[final]) == 1:
        ans.append(root)

    visit[final] = root

    return final
