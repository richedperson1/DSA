def finalDestination( n, m, k, roads):
    #code here  
    ans = 0
    def helperFun(ind,kk):
        if ind>=m:
            return 0
        
        if kk<k:
            index = roads[ind][1]-roads[ind][0]
            take = helperFun(ind+index,kk) + (roads[ind][1]-roads[ind][0])*roads[ind][-1]
            notT = helperFun(ind+index,kk+1) + ((roads[ind][1]-roads[ind][0])*(roads[ind][-1]//2))
            return min(take,notT)
        
        else:
            index = roads[ind][1]-roads[ind][0]
            return helperFun(ind+index,kk) + (roads[ind][1]-roads[ind][0])*roads[ind][-1]


    kk = 0
    ind = 0    
    return helperFun(ind,kk)

N = 4
M = 3
K = 1
Roads = [[0, 1, 10], [1, 2, 51], [0, 3, 5]]

print(finalDestination(N,M,K,Roads))