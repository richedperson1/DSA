"""
! URL : https://practice.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1
"""


#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, N):
        if N==1:
            return []
            
        ans = [True]*(N+1)
        
        for ind in range(2,N//2 +2):
            local = ind*2
            for check in range(local,N+1,ind):
                ans[check] = False

        print(ans)    
        final = []
        for ind,data in enumerate(ans):
            if ind<=1:
                continue
            
            elif data==True:
                final.append(ind)
            
        return final
    
obj = Solution()
print(obj.sieveOfEratosthenes(10))