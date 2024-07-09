class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        arr = [i+1 for i in range(n)]
        last = 0
        while len(arr)>1:
            
            # if k>len(arr):
            #     k = k%len(arr)


            for plus in range(k):
                last+=1
                last = last%len(arr)
            last-=1
            ele = arr.pop(last)
            if last==-1:
                last = 0
            last = last%len(arr)
        print(arr)
        return arr[0]
            

obj = Solution()

obj.findTheWinner(7,7)