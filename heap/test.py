from sortedcontainers import SortedList
nums = [4, 1, 5, 20, 3]
for i in range(len(nums)):

    if nums[i] & 1:
        nums[i] = nums[i]*2

nums = SortedList(nums)

result = 100000000000
max_value = 0
min_value = 0
while True:
    min_value = int(nums[0])
    max_value = int(nums[-1])

    if max_value & 1 == 0:
        nums.pop()
        nums.add(max_value // 2)
        max_value = nums[-1]
        min_value = nums[0]

        result = min(result, max_value - min_value)
    else:
        result = min(result, max_value - min_value)
        break


print(result)
