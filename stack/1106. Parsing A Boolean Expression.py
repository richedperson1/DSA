
expression = "&(!(f),|(f,f,f,f))"
true_false = {'t':True,"f":False}
exp = '!&|'


exp_stack = []

stack = []
size = len(expression)

for ind,char in enumerate(expression):
    if char in exp:
        exp_stack.append(char)
    elif char=="," or char==" ":
        continue
    elif char!= ")":
        if char in true_false:
            stack.append(true_false[char])
        else:
            stack.append(char)
        
    else:
        
        last_op = exp_stack.pop()
        
        if last_op=='!':
            
            ele = stack.pop()
            stack.pop()
        
            ele = not ele
            stack.append(ele)
        
        else:
            # try:
                final = stack.pop()
                # print(final)
                while stack and stack[-1]!="(" and last_op=="&":
                    second = stack.pop()
                    final = final and second
                    
                while stack and stack[-1]!="(" and last_op=="|":
                    second = stack.pop()
                    final = final or second
                
                stack.pop()
                stack.append(final)
            

print("===============> ",stack[0])
            
            
            
