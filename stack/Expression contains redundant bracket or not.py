def checkRedundancy( s):
    
    stack = []
    for char in s:
        if char==')':
            top = stack.pop()
            
            total = 0
            while top!="(":
                top = stack.pop()
                total+=1
                
            if total<1:
                return 1
        else:
            stack.append(char)

    return 0

s = '(b+c-d+(c))'


print(checkRedundancy(s))