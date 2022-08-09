"""
Given a stack with push(), pop(), empty() operations, delete the middle of the stack without using any additional data structure.
Middle: ceil((size_of_stack+1)/2) (1-based index)


Input: 
Stack = {1, 2, 3, 4, 5}
Output:
ModifiedStack = {1, 2, 4, 5}

Input: 
Stack = {1 2 3 4}
Output:
ModifiedStack = {1 3 4}
"""


class Solution:

    # Function to delete middle element of a stack.
    def function(self, s, i):
        if i == len(s):
            s.pop()
            return s
        ele = s.pop()
        arr = self.function(s, i)
        arr.append(ele)
        return arr

    def deleteMid(self, s, sizeOfStack):
        if (sizeOfStack)//2 == len(s):
            s.pop()
            return s
        ele = s.pop()
        self.deleteMid(s, sizeOfStack)
        s.append(ele)
        return s


arr = [1, 2, 3, 4]
obj = Solution()
print(obj.deleteMid(arr, len(arr)))
print(obj.function(arr, 2))
print((len(arr))//2)
