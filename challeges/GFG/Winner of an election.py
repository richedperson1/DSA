def winner(arr):
    # Your code here
    # return the name of the winning candidate and the votes he recieved
    vote = {}
    for data in arr:
        vote[data] = vote.get(data,0)+1
    
    maxi = 0
    for key,val in vote.items():
        maxi = max(val,maxi)
        
    
    ans = ""

    for key,val in vote.items(): 
        if val==maxi:
            if ans=='':
                ans = key
            ans = min(key,ans)
    return [ans,maxi]


arr = ['a','b','c']

print(winner(arr))