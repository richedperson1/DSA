
def majority(arr):
    majority = arr[0]
    count = 0
    for ind,data in enumerate(arr):
        if count==0:
            count+=1
            majority = arr[ind]

        elif majority==arr[ind]:
            count+=1
        else:
            count-=1

    return majority

arr = [2,2,2,1,3,4,5]

print(majority(arr))