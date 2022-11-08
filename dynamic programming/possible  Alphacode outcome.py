
"""

Alice and Bob need to send secret messages to each other and are discussing ways to encode their messages:

Alice: “Let’s just use a very simple code: We’ll assign ‘A’ the code word 1, ‘B’ will be 2, and so on down to ‘Z’ being assigned 26.”

Bob: “That’s a stupid code, Alice. Suppose I send you the word ‘BEAN’ encoded as 25114. You could decode that in many different ways!”

Alice: “Sure you could, but what words would you get? Other than ‘BEAN’, you’d get ‘BEAAD’, ‘YAAD’, ‘YAN’, ‘YKD’ and ‘BEKD’. I think you would be able to figure out the correct decoding. And why would you send me the word ‘BEAN’ anyway?”

Bob: “OK, maybe that’s a bad example, but I bet you that if you got a string of length 5000 there would be tons of different decodings and with that many you would find at least two different ones that would make sense.”

Alice: “How many different decodings?”
Bob: “Jillions!”


url: https://www.hackerearth.com/problem/algorithm/acode-alphacode-3/

"""
possible = "20212"
n = len(possible)-1

ans = []


def check_possible_1(string, local, ans):
    if string == "":
        ans.append(local)
        return

    single = string[0]
    if int(single) <= 9 and int(single) >= 1:
        check_possible_1(string[1:], local+[single], ans)

    if len(string) >= 2:
        double = single+string[1]
        if int(double) >= 10 and int(double) <= 26:
            check_possible_1(string[2:], local+[double], ans)


count_var = 0

"""
Time complexity : O(2^n)
Time complexity : O(2^n)
space complexity : O(n) {
    only stack space into the counts
}

"""


def check_var(string):
    global count_var
    count_var += 1
    if string == "":
        return 1

    single = string[0]
    ans = 0
    if int(single) <= 9 and int(single) >= 1:
        ans += check_var(string[1:])

    if len(string) >= 2:
        double = single+string[1]
        if int(double) >= 10 and int(double) <= 26:
            ans += check_var(string[2:])

    return ans


"""
Time complexity : O(n)
Time complexity : O(n+n) ~ O(n)

space complexity : O(n) {
    memoiztion and  stack space into the counts
}

"""


def check_var_using_dp(string, dp, i=0):
    global count_dp
    count_dp += 1
    if string == "":
        return 1
    if dp[i] != 0:
        return dp[i]
    single = string[0]
    ans = 0
    if int(single) <= 9 and int(single) >= 1:
        ans += check_var_using_dp(string[1:], dp, i+1)

    if len(string) >= 2:
        double = single+string[1]
        if int(double) >= 10 and int(double) <= 26:
            ans += check_var_using_dp(string[2:], dp, i+2)

    dp[i] = ans
    return ans


count_dp = 0
possible = "2222222222222"
n = len(possible)
dp = [0]*(n)

value = check_var(possible)
print("count using recursion approach", count_var)

ans = check_var_using_dp(possible, dp, 0)
print("count using dp approach", count_dp)
