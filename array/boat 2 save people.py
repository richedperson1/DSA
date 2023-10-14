def boatNeed(arr,limit):
    arr.sort()
    local = 0
    ans = 1
    for ind,data in enumerate(arr):
        if data==limit:
            ans+=1
            local = 0
        elif local+ data<= limit:
            local+=data
        else:
            local = data
            if local==limit:
                ans+=1
                local = 0
            ans+=1
    return ans




arr = [3,5,3,4,2,4,5,2,3,1,2,1,2,1,3,1,3,4,5,4,3,2,1,1]
limit = 5
print(boatNeed(arr,limit))