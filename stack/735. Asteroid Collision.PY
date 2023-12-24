class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        stack = []
        for data in arr:
            while stack and data<0 and stack[-1]>0:
                diff = data+stack[-1]
                if diff<0:
                    stack.pop()
                elif diff>0:
                    data = 0
                else:
                    data = 0
                    stack.pop()
            if data:
                stack.append(data)
        return stack