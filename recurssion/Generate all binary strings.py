"""
! URL : https://www.geeksforgeeks.org/generate-binary-strings-without-consecutive-1s
"""


def binaryStr(num):
    ans = []
    def generate(local,prev,ind):
        if ind>=num:
            ans.append(local)
            return ans

        if prev:
            generate(local+"0",False,ind+1)
        else:
            generate(local+"0",False,ind+1)
            generate(local+"1",True,ind+1)
        
        return ans
    
    return generate("",False,0)


print(binaryStr(4))