class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:

        arr = [0,0]

        for ind, data in enumerate(bills):
            if data==5:
                arr[0]+=1
            elif data==10:
                if arr[0]>0:
                    arr[0]-=1
                    arr[1]+=1
                else:
                    return False,1
            else:
                if arr[1]>0 and arr[0]>0:
                    arr[1]-=1
                    arr[0]-=1
                elif arr[0]>=3:
                    arr[0]-=3
                else:
                    print(ind)
                    return False,2
        return True

obj = Solution()
bills =[5,5,5,5,10,5,10,10,10,20]
print(obj.lemonadeChange(bills))