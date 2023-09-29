from typing import *

def merge( arr: List[List[int]]) -> List[List[int]]:
    
    arr.sort()

    ans =[]

    num = len(arr)
    for ind in range(num):
        start = arr[ind][0]
        end   = arr[ind][1]

        if len(ans)>0 and ans[-1][1]>= end:
            continue
        

        for j in range(ind,num):
            if end>=arr[j][0]:
                end = max(end,arr[j][1])
            else:
                break

        ans.append([start,end])

    return ans

def merge2( arr: List[List[int]]) -> List[List[int]]:
    
    arr.sort()

    ans =[arr[0]]

    num = len(arr)
    
    for ind in range(1,num):
        start = arr[ind][0]
        end   = arr[ind][1]
        if ans[-1][1]>= start:
            ans[-1][1] = max(ans[-1][1],end)
        else:
            ans.append([start,end])


    return ans
arr  = [[1,3],[2,6],[8,10],[15,18]]

print(merge(arr))
print(merge2(arr))