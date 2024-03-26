

def posOfRightMostDiffBit(m,n):
    if m==n:
        return -1
    count = 0
    while m>0 and n>0:
        if not(m&1 ==n&1):
            count+=1
            
        m = m>>1
        n = n>>1
    
    return count
        
print(posOfRightMostDiffBit(9,11))