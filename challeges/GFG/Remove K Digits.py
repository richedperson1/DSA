class Solution:

    def removeKdigits(self, S, k):
        stack = []
        
        for data in str(S):
            while stack and stack[-1]>data and k>0:
                stack.pop()
                k-=1
            
            if stack or data!='0':
                stack.append(data)
         
                    
        print(stack,k)
        if k>0:
            stack = stack[:-k]
            
        return ''.join(stack) if stack else "0"
        

    def removeKdigits2(self, S, k):
        stack = []
        
        for data in str(S):
            
            while stack and stack[-1]>data and k>0:
                stack.pop()
                k-=1
            
            if stack or data!='0':
                stack.append(data)
         
                    
        print(stack,k)
        if k>0:
            stack = stack[:-k]
            
        return ''.join(stack) if stack else "0"
        
        
obj = Solution()
s = "149811"
k = 3
print(obj.removeKdigits(s,k))