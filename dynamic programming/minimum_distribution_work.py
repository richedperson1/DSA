arr = [3, 2, 3, 2, 3, 5, 1, 3]

n = len(arr)
minimum = [0] * n
minimum[0] = arr[0]
minimum[1] = arr[1]
minimum[2] = arr[2]

for j in range(3, n):
    mini = min(minimum[j-1], minimum[j-3], minimum[j-2])+arr[j]
    minimum[j] = mini

print(minimum)
