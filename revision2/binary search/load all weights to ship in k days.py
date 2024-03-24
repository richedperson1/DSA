def shipWithinDays( weights: list[int], days: int):

    def isPossible2load(decideWeight,weights,days):

        local = 0
        lDays = 1
        for ind,data in enumerate(weights):
            if data>decideWeight:
                return False
            elif local+data>decideWeight:
                local = data
                lDays+=1
                if lDays>days:
                    return False
                
            else:
                local+=data

        return True

    
    
    low,high = 0,sum(weights)
    ans = float("inf")
    while low<high:
        mid = (low+high)//2 
        if isPossible2load(mid,weights,days):
            ans = min(ans,mid)
            high = mid-1
        else:
            low = mid+1

    return ans


weights = [1,2,3,4,5,6]

days = 2

print(shipWithinDays(weights,days))