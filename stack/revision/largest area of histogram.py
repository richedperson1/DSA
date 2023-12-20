#User function Template for python3

def stack_made(arr):
    l_stack = []
    
    ans = []
    for ind,data in enumerate(arr):
        if not l_stack:
            ans.append(-1)
            l_stack.append(ind)
        else:
            while l_stack and arr[l_stack[-1]]>=data:
                l_stack.pop()
                
            if l_stack:
                ans.append(l_stack[-1])
            else:
                ans.append(-1)
            
            l_stack.append(ind)
    
    return ans
    

    #Function to find largest rectangular area possible in a given histogram.
def getMaxArea(arr):
    #code here
    first = stack_made(arr)
    
    ans1 = []
    stack = []
    
    result = 0
    
    size = len(arr)
    for ind in reversed(range(size)):
        if not stack:
            ans1.append(-1)
            stack.append(ind)
        else:
            while stack and arr[stack[-1]]>=arr[ind]:
                stack.pop()
            
            if not stack:
                ans1.append(-1)
            else:
                ans1.append(stack[-1])
            
            stack.append(ind)
    
    ans1 = ans1[::-1]
    total = 0
    for ind,data in enumerate(zip(first,ans1)):
        left,right = data
        if right==-1:
            total = (size-left-1)*arr[ind]
            result = max(total,result)
        else:
            total = (right-left-1)*arr[ind]
            result = max(total,result)
    return result

arr = list(map(int,'9 10 4 10 4 5 16'.split()))
print(arr)

print(getMaxArea(arr))