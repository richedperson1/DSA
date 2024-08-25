#User function Template for python3

class Solution:
    
     #Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(self,arr,brr):
        #code here
        a = len(arr)
        b = len(brr)
        x = [i ** (1 / i) for i in arr]
        y = [i ** (1 / i) for i in brr]
        x.sort()
        y.sort()
        print(arr,brr)
        print(x,y)
        c, j = 0, 0
        for i in range(a):
            while j < b and x[i] > y[j]:
                j += 1
            c += j
        return c
    
    
obj = Solution()

arr = [2,1,6]
brr = [1,5]

print(obj.countPairs(arr,brr))