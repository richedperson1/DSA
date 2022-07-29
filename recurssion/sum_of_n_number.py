"""
Calculate the sum of first n natural number using recurssion
n : user define integers.
return : sum of n number

Only used recurssion for it !
"""

n = 110
# Sum of n number using recurssion


def sum_of_n(n):
    if n <= 1:
        return n
    small = sum_of_n(n-1)
    return n+small

# using formula


def sum_n(n):
    return int((n*(n+1))/2)


print(sum_of_n(n))
print(sum_n(n))
