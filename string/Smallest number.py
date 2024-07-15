def smallest_num(s,d):
    
    def small_num(s,d):
        maxv=9*d
        if s>maxv: 
            return -1
        ans=""
        # s-=1
        for i in range(0,d):
            if s>=9:
               ans+=str(9)
               s-=9
            else:
                ans+=str(s)
                s=0
              
        ans=ans[::-1]
        return ans
            
    return small_num(s,d)


s = 18
d = 2

print(smallest_num(s,d))