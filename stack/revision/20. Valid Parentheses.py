def isValidOptimal( s: str) -> bool:
    stack = []
    opn = '([{'
    cls = {")":'(',
            "}":'{',
            "]":"["}
    for data in s:
        if data in opn:
            stack.append(data)
        else:
            if stack:
                opn1 = cls.get(data,"")
                if opn1=='':
                    return False
                elif stack[-1]==opn1:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                return False
    return True if not stack else False

def isValid( s: str) -> bool:
    stack = []
    opn = '([{'
    cls = {")":'(',
            "}":'{',
            "]":"["}
    
    result = 0
    total = 0
    for data in s:
        if data in opn:
            stack.append(data)
        else:
            if stack:
                opn1 = cls.get(data,"")
                if stack[-1]==opn1:
                    total+=2
                    result = max(total,result)
                    stack.pop()
                    
                else:
                    stack = []
                    total = 0
            else:
                total = 0
    return result


vlaid = "))))()))()))))(())())())())))))))()(()(()(()()(((((()((()())())(())()()))()()()()()((()())()((()()((((()(((()))(()))()((()()(())()()()))()())((((())(()))()()()((())))(())())))(())(()((()()((())()))())"

vlaid = "(((())"
print(isValid(vlaid))