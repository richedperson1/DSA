
"""
Time complexity : O(n)
Space complexity : O(n)
"""

def missing(a):
    duplicate = {}
    duplicateNum = ""
    misssingNum = ""
    for ind,data in enumerate(a):
        if data in duplicate:
            duplicate[data]+=1
            duplicateNum = data
        else:
            duplicate[data] = 1
    

    for ind in range(1,len(a)+1):
        
        if duplicate.get(ind,-1)==-1:
            misssingNum = ind

    return [duplicateNum,misssingNum]


"""
Time complexity : O(n)
Space complexity : O(1)
"""
def missingDuplicate(arr): 
    
    size = len(arr)
    nSum = (size*(size+1))//2
    n2Sum =(size*(size+1)*(2*size+1))/6

    nSumArr = 0
    n2SumArr = 0
    
    for ind ,data in enumerate(arr):
        nSumArr+=data
        n2SumArr+= (data*data)

    
    xMinusY =  nSumArr   - nSum
    x2MinusY2 = n2SumArr - n2Sum

    xPlusY = x2MinusY2//xMinusY

    missing,duplicat = int((xMinusY+xPlusY)//2),int((xPlusY-xMinusY)//2)
    return [missing,duplicat]


arr = [1,2,3,3]

print(missingDuplicate(arr))