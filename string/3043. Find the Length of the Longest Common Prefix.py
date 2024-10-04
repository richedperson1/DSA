arr1 = [1,10,100] 

arr2 = [1000]

size = len(arr2)
result = 0
for ind,data in enumerate(arr1):
    for ind2 in range(size):
        data2 = str(arr2[ind2])
        data = str(data)
        if data.startswith(data2) or data2.startswith(data):
            local = min(len(data),len(data2))
            result = max(result,local)

print(result)


