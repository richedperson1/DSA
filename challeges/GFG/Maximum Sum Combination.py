def maxCombinations( n, k, a,b):
    
    a.sort()
    b.sort()
    
    ind1,ind2 = n-1,n-1
    
    ans = [a[-1]+b[-1]]
    
    ind1-=1
    ind2-=1
    k-=1
    common = ind1
    while k>0:
        
        local1 = a[-1]+b[ind2]
        local2 = b[-1]+a[ind1]
        local3 = a[common]+b[common]
        common-=1
        if a[-1]+b[ind2]>b[-1]+a[ind1]:
            ans.append(a[-1]+b[ind2])
            ind2-=1
        
        else:
            ans.append(b[-1]+a[ind1])
            ind1-=1
            
        k-=1
        

    return ans


import heapq
def maxCombinations( N, K, A, B):
    res=[]
    
    A.sort(reverse=True)
    B.sort(reverse=True)
    heap = []
    heapq.heappush(heap,(-(A[0]+B[0]),0,0))
    visited=set((0,0))
    while(K):
        sum,i,j=heapq.heappop(heap)
        res.append(-sum)
        if i+1<N and (i+1,j) not in visited:
            heapq.heappush(heap,(-(A[i+1]+B[j]),i+1,j))
            visited.add((i+1,j))
        if j+1<N and (i,j+1) not in visited:
            heapq.heappush(heap,(-(A[i]+B[j+1]),i,j+1))
            visited.add((i,j+1))
        K-=1
    return res


def maxCombinations2(n,k,a,b):
    a.sort()
    b.sort()
    ans = []
    heap = []
    
    heapq.heappush(heap,(-(a[-1]+b[-1]),n-1,n-1))
    visited = set((n-1,n-1))

    while k>0:
        sumi,i,j  = heapq.heappop(heap)
        k-=1
        ans.append(-sumi)

        if i-1>=0 and (i-1,j) not in visited:
            heapq.heappush(heap,(-(A[i-1]+B[j]),i-1,j))
            visited.add((i-1,j))
        if j-1>=0 and (j-1,j) not in visited:
            heapq.heappush(heap,(-(A[i]+B[j-1]),i,j-1))
            visited.add((i,j-1))

    return ans
N = 17
K = 6
A =  [1, 4, 2, 3]
B  = [2, 5, 1, 6]

A = [46, 104, 159, 331, 343, 349, 371, 469, 512, 552, 572, 608, 719, 721, 830, 890, 917] 
B =[150, 203, 209, 253, 273, 389, 404, 595, 597, 658, 666, 681, 778, 847, 898, 959, 965]

print(maxCombinations(N,K,A,B))
print(maxCombinations2(N,K,A,B))