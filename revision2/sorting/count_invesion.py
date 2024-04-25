
import sys

sys.setrecursionlimit(10**8)
class Solution:
    inversion = 0
    def inversionCount(self, arr, n):
        # Your Code Here
        
        def mergerInversion(brr):

            if len(brr)<=1:
                return 
            
            mid = len(brr)//2
            
            leftSide = brr[:mid]
            rightSide = brr[mid:]
            mergerInversion(leftSide)
            mergerInversion(rightSide)
            sizeR = len(rightSide)
            sizeL = len(leftSide)
            sizeT = len(brr)
            
            r,l,t = 0,0,0
            
            while r<sizeR and l <sizeL:

                if leftSide[l]> rightSide[r]:
                    self.inversion+=(sizeL-l)
                    
                    brr[t] = rightSide[r]
                    r+=1
                    t+=1
                
                else:
                    brr[t] = leftSide[l]
                    l+=1
                    t+=1
                    
            
            while r<sizeR:
                brr[t] = rightSide[r]
                r+=1
                t+=1
                
            while l<sizeL:
                brr[t] = leftSide[l]
                l+=1
                t+=1
            return brr
        mergerInversion(arr)
        return self.inversion


arr = [468, 335, 1, 170, 225, 479, 359, 463, 465, 206, 146, 282, 328, 462, 492, 496, 443, 328, 437, 392, 105, 403, 154, 293, 383, 422, 217, 219, 396, 448, 227, 272, 39, 370, 413, 168, 300, 36, 395, 204, 312, 323]
obj = Solution()
print(obj.inversionCount(arr,len(arr)))