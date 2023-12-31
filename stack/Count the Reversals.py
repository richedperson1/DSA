import math
def countRev (s):
    if len(s)&1:
        return -1
    close = 0
    opn = 0
    total = 0
    for char in s:
        if char=="{":
            opn+=1
        else:
            if opn>0:
                opn-=1
            else:
                close+=1
        
    total = math.ceil(opn/2)+math.ceil(close/2)    
    return total


string = "{{}{{{}{{}}{{"


print(countRev(string))