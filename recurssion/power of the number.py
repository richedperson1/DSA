
def power(a, n):
    if n == 1:
        return a
    if n == 0:
        return 1

    ans = power(a, n//2)
    if n & 1:
        return a*ans*ans
    else:
        return ans*ans


a = int(input("Enter a value : "))
n = int(input("Enter b value : "))
print(power(a, n) == a**n)
