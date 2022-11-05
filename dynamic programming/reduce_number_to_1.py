"""
Minimum number of operations required to reduce N to 1

n = number
1. Subtract number by 1 ie. n-1<=n

2. divide by 2 if it divisible by 2

3. divide by 3 if it divisible by 3


find minimum number of way by which it reduce to 1


answer :

In this Quection, they are asking about height of tree under above three condition

Which means which node side will give us small height
"""

import sys
num = 50
ans = 4654584141


# def reduce(num, i, ans):
#     if num <= 1:
#         ans = min(ans, i)
#         return ans

#     l1 = 544198498
#     l2 = 544198498
#     if num % 3 == 0:
#         l1 = reduce(num//3, i+1, ans)

#     if num % 2 == 0:
#         l2 = reduce(num//2, i+1, ans)

#     l3 = reduce(num-1, i+1, ans)

# return min(l1, l2, l3)


# print(reduce(num, 0, ans))


# num = 50


# def reduce_num(num, i, ans, dp):
#     if num <= 1:
#         return min(ans, i)

#     if dp[num] != 0:
#         return dp[num]

#     l1 = 544198498
#     l2 = 544198498
#     l3 = 544198498
#     if num % 3 == 0:
#         l1 = reduce_num(num//3, i+1, ans, dp)
#         ans = abs(i-l1)
#         dp[num] = i+ans
#     if num % 2 == 0:
#         l2 = reduce_num(num//2, i+1, ans, dp)
#         ans = abs(i-l2)
#         dp[num] = i+ans

#     l3 = reduce_num(num//2, i+1, ans, dp)
#     dp[num] = l3

#     return min(l1, l2, l3)


# num = 50
# i = 0
# ans = 4546551651
# dp = [0]*(num+1)
# final = reduce_num(num, i, ans, dp)
# print(final)


"""
reduce number to 1 using bottom to top approach
"""
count = 0


def reduce_num_2_1(num):
    global dp, count
    count += 1
    if num <= 1:
        return 0

    l1 = sys.maxsize
    l2 = l1
    l3 = l1
    if num % 3 == 0:
        l1 = reduce_num_2_1(num//3)
        l1 = l1+1

    if num % 2 == 0:
        l2 = reduce_num_2_1(num//2)+1

    l3 = reduce_num_2_1(num-1)+1
    return min(l1, l3, l2)


count2 = 0


def reduce_num_using_dp(num):
    global dp
    global count2
    count2 += 1
    if num <= 1:
        return 0

    l1 = sys.maxsize
    l2 = l1
    l3 = l1
    if dp[num] != 0:
        return dp[num]
    if num % 3 == 0:
        l1 = reduce_num_using_dp(num//3)
        l1 = l1+1

    if num % 2 == 0:
        l2 = reduce_num_using_dp(num//2)+1

    l3 = reduce_num_using_dp(num-1)+1
    mini = min(l1, l3, l2)
    dp[num] = mini
    return mini


num = 1000
dp = [0]*(num+1)

# print()
# print("Final answer is without dp : ", reduce_num_2_1(num))
# print("Number of count ", count)
# print()
# print("--"*30)
# print()
# ans = reduce_num_using_dp(num)
# print("Answer is : ", ans)
# print("Number of count using dp :", count2)


# print(reduce_num_2_1(num)).
"""
DP using tabulation

Time complexity : O(n)
Space complexity : O(n)

"""


def reduce_num_table(num):
    if num <= 1:
        return 0
    dp = [0]*(num+1)

    dp[2] = 1
    dp[3] = 1

    for i in range(4, num+1):
        a = sys.maxsize
        b = a
        c = a
        if i % 2 == 0:
            a = dp[i//2]+1
            # print("a----->", a)
        if i % 3 == 0:
            b = dp[i//3]+1
        c = dp[i-1]+1

        dp[i] = min(a, b, c)
    return dp


num = 10
print(reduce_num_table(num))
