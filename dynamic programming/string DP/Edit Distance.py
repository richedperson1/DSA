

def edit_dist(s1,s2):
    n1, n2 = len(s1), len(s2)
    dp = {}
    def recursive_call(ind1,ind2):
        if ind1 >= n1:
            return max(0, n2-ind2)

        if ind2 >= n2:
            return max(0, n1-ind1)
        
        if (ind1,ind2) in dp:
            return dp[(ind1,ind2)]
        
        if s1[ind1]==s2[ind2]:
            dp[(ind1,ind2)] =  recursive_call(ind1+1,ind2+1)
            return dp[(ind1,ind2)] 
        
        else:
            first = recursive_call(ind1+1,ind2+1)+1 # replace
            second = recursive_call(ind1+1,ind2)+1  #remove letter
            third = recursive_call(ind1,ind2+1)+1    # insert
            
            local_ans =  min(first,second,third)
            
            dp[(ind1,ind2)] = local_ans
            return local_ans
    return recursive_call(0,0)


# s1 = 

str1 = "geek"
str2 = "gesek"

print(edit_dist(str1,str2))