num = 14


previous = [0]*(num+1)

previous[1] = 1


for i in range(num+1):
    previous[i] = previous[i//2] + i % 2


print(previous)
