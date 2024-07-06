
class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.val = data

    def __repr__(self) -> str:
        return str(self.data)

class linked_list_maker:
    def __init__(self, head=None):
        if head == None:
            self.head = None
        else:
            self.head = head
    def create_ll(self, arr=[2, 4, 5, 6, 8, 9]):
        flag = False

        if self.head == None:
            first_node = node(arr[0])
            flag = True
            curr = first_node
            self.head = curr
        else:
            flag = False
            curr = self.head
        while curr.next:
            curr = curr.next
        if flag:
            for ind, num in enumerate(arr):
                if ind == 0:
                    continue
                new = node(num)
                # print(curr)
                curr.next = new
                curr = new
        else:
            for num in arr:
                new = node(num)
                curr.next = new
                curr = new
        self.tail = new
        return self.head    

class Solution:
    def nodesBetweenCriticalPoints(self, head:list[int]) -> list[int]:
        ind = 2
        result = []
        prev = head
        head = head.next
        mini = float("inf")
        while head and head.next:
            if head.val>prev.val and head.val>head.next.val:
                result.append(ind)
            elif head.val<prev.val and head.val<head.next.val:
                result.append(ind)
            ind+=1

            
            if len(result)>=2:
                mini = min(mini,result[-1] - result[-2])
            prev = head
            head = head.next
        print(result)
        if len(result)>=2:
            return [mini,result[-1]-result[0]]
        

        if len(result)==1:
            return [-1,result[-1]]
        
        return [-1,-1]
    

obj = Solution()
# arr = [5,3,1,2,5,1,2,25,6,6,9,8,3,5,4]
arr = [5,3,1,2,5,1,2,25,6,6,9,8,3,5,4]
linked = linked_list_maker().create_ll(arr)

print(obj.nodesBetweenCriticalPoints(linked))