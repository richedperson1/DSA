def AllParenthesis(n):
    #code here
    ans = []
    def generator(ind,clg,opn,local):
        if clg==n and opn==n:
            
            ans.append(local)
            
            return
        if clg > opn or opn > n:
            return
        
        generator(ind+1,clg,opn+1,local+"(")
        generator(ind+1,clg+1,opn,local+")")
    
    generator(0,0,0,"")
    return ans


# def AllParenthesis(n):
#     #code here
#     ans = []
#     ap(n, n, "", ans)
#     return ans
    
# def ap( o, c, s, ans):
    
#     if o == 0 and c == 0:
#         ans += [s]
#         return
    
#     if c < o or o < 0:
#         return
    
    
#     ap(o-1, c, s + "(", ans)
    
#     ap(o, c-1, s + ")", ans)

print(AllParenthesis(3))