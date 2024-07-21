
def move_negative_at_left( arr):
    # Write your code here
    size = len(arr)
    neg = 0
    pos = size-1
    ind = 0
    
    while ind<pos and neg < pos:
        if arr[ind]<0:
            arr[neg],arr[ind] = arr[ind],arr[neg]
            neg+=1
            ind+=1
        
        elif arr[ind]>=0:
            arr[pos],arr[ind] = arr[ind],arr[pos]
            pos-=1
        
        else:
            ind+=1

    print(arr,)
    
def move_neg_po(arr):

        if len(arr)<=1:
            return arr[0]
        # Write your code here
        ans, maxneg, mod = 1, float('-inf'), 10**9+7
        flag = 0
        neg_num = 0
        zero = 0
        for data in arr:
            if data==0:
                zero+=1
            if data<0:
                neg_num+=1
            if data!=0:
                ans*= data
                flag = 1
            
            if data<0 and data>maxneg:
                maxneg = data
                
        if ans<0 and neg_num>1:
            ans//=maxneg
        
        if flag==0:
            return 0
        if ans>0:
            ans = ans%mod
        if zero:
            ans = max(ans,0)
        return ans


    
arr = [1,3,-5,51,3,-2,3]
arr = [1,3,-5,0,51,3,-2]
arr = [-1,0,-2,4,3]
# arr = [-1,0]
arr = [0,0,0,0]
arr = [-1,0]

print(move_neg_po(arr))