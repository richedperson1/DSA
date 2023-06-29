"""
! URL : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

"""
Time complexity : O(n)
Space complexity : O(n)
"""
def spaceTake(head,num):
    dist = []
    curr = head
    while curr:
        dist.append(curr)
        curr = curr.next
    total = len(dist)
    indR = total-num
    # print(dist)
    if num<=1:
        dist.pop()
    else:
        dist.pop(indR)
    if len(dist)<=0:
        return None
    head = dist[0]
    curr = head
    for ind in range(1,len(dist)):
        head.next = dist[ind]
        head = dist[ind]
    head.next = None
    return curr

"""
Time complexity : O(n)

Space complexity : O(1)

"""
def withoutSpace(head,n):
    curr = head
    total = 0
    while curr:
        total+=1
        curr = curr.next

    ind = total-n
    
    def removeNth(head,num):
        if not head:
            return head

        if ind==num:
            if head.next :
                return head.next
            else:
                return None

        head.next = removeNth(head.next,num+1)
        return head
    final = removeNth(head,0)
    return final

def optimizeSol(head,n):

    curr = head
    total = 0
    while curr:
        total+=1
        curr = curr.next

    ind = total-n
    
    def removeNth(head,num):
        if num==0:
            return head.next
        
        for index in range(1,total):
            if index==ind:
                
                continue

        if ind==num:
            if head.next :
                return head.next
            else:
                return None

        head.next = removeNth(head.next,num+1)
        return head
    final = removeNth(head,0)
    return final