"""
Given interger x and n. we have to complete function of calculate power

x^n -->  y
This we need to solve 

Input:

x = 5
n = 2

Output:

y = 25
"""


def cal_power(x, n):
    if n == 1:
        return x
    small = cal_power(x, n-1) % (10e9+7)
    return (x % (10e9+7)*small) % (10e9+7)


print(cal_power(2, 5))


def divide_and_conquer(num, power):
    if power == 1:
        return num

    else:
        mid = power//2
        ans = divide_and_conquer(num, mid)
        c = ans*ans        # Smart move to calculate tree output
        if power & 1 == 1:
            return (c*num) % 10e9+7
        else:
            return c % 10e9+7


n = 223
r = int(str(n)[::-1])
# print(divide_and_conquer(n, r) == cal_power(n, r))

print(divide_and_conquer(n, r))
print(cal_power(n, r))

print(686524215/2)
