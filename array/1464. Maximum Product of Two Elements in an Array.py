def maxProduct( nums: list[int]) -> int:
    first,second = 0,0

    for data in nums:
        if data>=first:
            second = first
            first = data

        elif data>second and first>data:
            second = data

    print(first,second)
    return (first-1)*(second-1)


arr = [10,2,5,2]

print(maxProduct(arr))
