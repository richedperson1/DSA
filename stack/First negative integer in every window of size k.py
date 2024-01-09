from collections import deque 

def printFirstNegativeInteger(arr, n, k):
    dq = deque([])
    ans = []

    for ind in range(min(k, n)):
        if arr[ind]<0:
            dq.append(ind)
        

    if len(dq)>0:
        ans.append(arr[dq[0]])
    else:
        ans.append(0)
    # Process the remaining windows
    for ind in range(k, n ):
        # Remove the element that is no longer in the current window
        if arr[ind]<0:
            dq.append(ind)
        
        if dq and dq[0]<=ind-k :
            dq.popleft()

        # Add the new element to the window
        if len(dq)>0:
            ans.append(arr[dq[0]])
        else:
            ans.append(0)
            

    return ans


arr = [1,-2,-3,5,4,-4,6,9]

k = 3
n = len(arr)

print(printFirstNegativeInteger(arr, n, k))