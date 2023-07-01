def sortedFun( s):
    
    def firstSort(s1,num):
        if s1==[]:
            return [num]
        
        if s1[-1]>num:
            s1.append(num)
            return s1
    
        ele = s1.pop()
        s1 = firstSort(s1,num)
        s1.append(ele)
        return s1
    
    def secondSort(s):
        new = []
        for ind ,data in enumerate(s):

            new = firstSort(new,s[-(ind+1)])
        return new
    return secondSort(s)


s = [1,2,3,4,5,10,6,3]
print(sorted(s))
print(sortedFun(s))