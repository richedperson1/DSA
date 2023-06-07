

"""

12 60 64
9 11 19 26 32 34 45 50 56 58 61 88
1 5 5 7 9 9 11 13 13 15 18 19 19 20 21 28 28 28 29 29 30 31 39 40 44 47 47 50 52 56 57 61 61 61 66 68 69 70 70 74 75 75 77 78 79 80 82 85 87 89 90 90 90 92 93 95 97 98 98 100
"""

arr = list(map(int,"9 11 19 26 32 34 45 50 56 58 61 88".split()))
brr = list(map(int,"1 5 5 7 9 9 11 13 13 15 18 19 19 20 21 28 28 28 29 29 30 31 39 40 44 47 47 50 52 56 57 61 61 61 66 68 69 70 70 74 75 75 77 78 79 80 82 85 87 89 90 90 90 92 93 95 97 98 98 100".split()))
k = 64
n,m = len(arr),len(brr)



"""
Time complexity : O(n)
Space complexity : O(n)
"""

def kthElementNaive(  arr1, arr2, n, m, k):
        
        final = []
        
        i1 = 0
        i2 = 0
        total = 0
        while i1<n and i2<m:
            total+=1
            if arr1[i1]<=arr2[i2]:
                final.append(arr1[i1])
                i1+=1
            else:
                final.append(arr2[i2])
                i2+=1
        
            if total==k:
                print("first")
                return final[k-1]

        while i1<n :
            total+=1
            final.append(arr1[i1])
            i1+=1
            if total==k:
                
                return final[k-1]
            
        while i2<m:
            total+=1
            final.append(arr2[i2])
            i2+=1
            if total==k:
                return final[k-1]
 
        if total==k:
            
            return final[k-1]
        


"""
Time complexity : O(n)
Space complexity : O(1)
"""

        
def kthElementOptimize(arr1, arr2, n, m, k):     
    i1 = 0
    i2 = 0
    total = 0
    ans = 0
    while i1<n and i2<m:
        total+=1
        if arr1[i1]<=arr2[i2]:
            ans = arr1[i1]
            i1+=1
        else:
            ans = arr2[i2]
            i2+=1
    
        if total==k:
            return ans

    while i1<n :
        total+=1
        ans = arr1[i1]
        i1+=1
        if total==k:
            
            return ans
        
    while i2<m:
        total+=1
        ans = arr2[i2]
        i2+=1
        if total==k:
            return ans
 
print(kthElementOptimize(arr,brr,n,m,k))
new = sorted(arr+brr)

print(new[k])