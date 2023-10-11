
"""
! URL : https://leetcode.com/problems/maximum-swap/
"""
def maximumSwap( num ) :
    num = list(map(int,str(num)))
    size = len(num)
    leftMax = [0]*size
    local = (num[-1]),size-1
    for ind in reversed(range(size)):
        if local[0] < (num[ind]):
            local = max(local[0],(num[ind])),ind
            leftMax[ind] = local
        else:
            leftMax[ind] = local
    
    print(leftMax,num)
    mini = (num[0])
    for ind in range(size):
        mini = min((num[ind]), mini)
        if mini < (leftMax[ind][0]):
            num[ind],num[leftMax[ind][1]] = num[leftMax[ind][1]],num[ind]
            break

    newData = ""
    print(num)
    for data in num:
        newData+= str(data)
    
    return int(newData)


print(maximumSwap(8657))


