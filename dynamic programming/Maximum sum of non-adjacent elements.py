"""
You are given an array/list of ‘N’ integers. You are supposed to return the maximum sum of the subsequence with the constraint that no two elements are adjacent in the given array/list

url : https://www.codingninjas.com/codestudio/problems/maximum-sum-of-non-adjacent-elements_843261

inspired by love babbar

author : rutvikjaiswal195@gmail.com

"""
string = "0 85 12 89 7 91 73 39 65 52 17 12"
arr = list(map(int, string.split()))

# Method 1

"""
In this method we are using local arr for storing 

Time complexity : O(2^n)
space complexity: O(n)
"""


def maximum_sum_(arr, local, ans, i, flag):
    if i >= len(arr):
        ans.append(sum(local))
        return ans

    if flag:
        maximum_sum_(arr, local, ans, i+1, False)

    else:
        maximum_sum_(arr, local + [arr[i]], ans, i+1, True)
        maximum_sum_(arr, local, ans, i+1, False)


ans = []
# maximum_sum_(arr, [], ans, 0, False)
# print(max(ans))


"""
In this method we are using varible for storing previous summetion

Time complexity : O(2^n)
space complexity: O(1)

"""
count1 = 0


def maximum_sum_var(arr, local, ans, i, flag):
    if i >= len(arr):
        ans = max(ans, local)
        return ans

    if flag:
        ans = maximum_sum_var(arr, local, ans, i+1, False)

    else:
        ans = maximum_sum_var(arr, local + arr[i], ans, i+1, True)
        ans = maximum_sum_var(arr, local, ans, i+1, False)

    return ans


ans = 0


def maximum_sum_var2(arr, local, ans, i,):

    if i >= len(arr):
        ans = max(ans, local)
        return ans

    ans = maximum_sum_var2(arr, local + arr[i], ans, i+2)
    ans = maximum_sum_var2(arr, local, ans, i+1)

    return ans


ans = 0
# print(maximum_sum_var(arr, 0, 0,.

"""
Time complexity : O(n^2)
Time complexity : O(n)
"""


def maximum_sum_dp(arr):
    if len(arr) <= 1:
        return sum(arr)

    dp = [arr[0], arr[1]]

    first_max = arr[0]
    second_max = arr[1]
    n = len(arr)
    for i in range(2, n):
        maxi = max(max(dp[:i-1]) + arr[i], first_max+arr[i])
        dp.append(maxi)
        first_max = max(second_max, first_max)
        second_max = max(arr[i], second_max)
    return max(dp)


# print(maximum_sum_dp(arr))

counting = 0


def maximum_sum_using_dp(arr, dp, n):
    global counting
    counting += 1
    if n < 0:
        return 0
    if n == 0:
        return arr[0]

    if dp[n] != 0:
        return dp[n]

    include = maximum_sum_using_dp(arr, dp, n-2)+arr[n]
    exclued = maximum_sum_using_dp(arr, dp, n-1)+0

    dp[n] = max(include, exclued)
    return dp[n]


def FindMaxSum(arr):
    n = len(arr)
    dp = [0]*(n+4)

    for i in range(n-1, -1, -1):
        ans1 = dp[i+2]+arr[i]
        ans2 = dp[i+1]
        dp[i] = max(ans1, ans2)
    return dp[0]


def findMaxSumTabOptimize(arr):
    first = 0
    second = 0
    n = len(arr)
    curr = 0
    for i in range(n-1, -1, -1):
        ans1 = second+arr[i]
        ans2 = first
        curr = max(ans1, ans2)
        second = first
        first = curr

    return max(first, second)


num = len(arr)
dp = [0]*(num+1)
print(maximum_sum_using_dp(arr, dp, num-1))
print(counting)

"""

input : 

100
10
11 55 17 23 97 11 3 64 45 25
10
84 83 7 82 97 67 74 87 57 16
10
0 85 12 89 7 91 73 39 65 52
10
1 51 70 19 82 25 57 77 26 3
10
69 49 61 55 5 29 54 71 3 36
10
94 7 11 31 70 91 72 12 41 44
10
82 79 35 0 99 26 62 67 63 76
10
52 19 90 32 2 13 16 8 59 45
10
26 26 79 64 23 72 7 60 48 58
10
21 87 32 13 83 93 85 88 6 77
10
55 24 60 17 36 59 19 53 4 0
10
73 51 65 74 83 73 89 27 36 44
10
59 48 78 83 61 14 61 95 42 78
10
45 46 82 9 36 14 73 52 60 63
10
62 30 85 83 56 33 58 73 98 10
10
87 61 20 4 61 55 84 0 11 59
10
36 89 11 32 26 30 18 53 23 74
10
5 32 46 11 32 14 92 96 36 82
10
99 1 15 69 70 24 81 99 83 49
10
11 8 8 3 8 10 86 31 83 80
10
70 39 71 55 86 96 82 25 45 50
10
38 53 20 95 5 44 0 3 51 75
10
65 7 76 90 78 47 8 91 59 84
10
53 81 28 57 56 70 11 28 81 86
10
2 53 92 66 54 100 96 18 29 77
10
98 36 70 34 36 24 4 72 33 87
10
52 30 92 8 69 77 96 3 65 52
10
71 27 100 88 87 84 40 14 76 16
10
45 55 63 73 84 53 72 68 49 38
10
50 61 95 84 14 31 30 2 78 90
10
4 59 40 32 75 72 22 26 75 12
10
12 70 46 44 33 44 2 96 46 35
10
47 44 44 42 14 21 41 68 90 90
10
84 87 21 88 58 49 90 38 24 69
10
85 43 68 87 39 65 25 8 93 15
10
65 88 70 81 31 48 2 36 89 23
10
1 76 31 85 7 78 67 22 4 54
10
8 53 69 82 23 85 77 6 76 39
10
40 12 31 93 41 76 42 32 50 58
10
42 42 0 2 69 91 64 59 55 94
10
31 32 9 71 76 13 37 72 35 62
10
13 19 63 66 7 53 76 9 78 45
10
2 52 54 100 54 30 61 2 48 71
10
49 25 19 48 98 68 70 15 47 71
10
52 25 52 19 0 77 84 9 78 65
10
88 81 82 12 88 49 17 86 6 66
10
88 51 22 73 86 22 21 50 20 8
10
65 1 84 58 19 36 93 19 99 47
10
87 33 59 11 49 8 42 20 56 22
10
1 40 75 41 73 24 40 35 3 63
10
13 23 26 61 20 43 57 5 60 72
10
92 77 23 43 70 84 54 9 27 66
10
27 53 10 29 59 100 35 61 73 35
10
94 20 10 86 86 39 54 12 7 36
10
90 16 41 14 61 53 71 95 80 77
10
58 41 75 63 57 75 30 35 88 20
10
98 47 7 80 42 49 18 84 5 62
10
74 95 84 10 68 56 73 46 23 44
10
88 77 77 90 51 69 87 26 12 6
10
84 17 12 81 74 91 65 33 55 55
10
2 89 23 36 3 99 35 3 54 71
10
89 60 30 92 27 12 33 90 4 17
10
13 19 70 81 5 52 78 39 12 86
10
70 27 23 14 71 77 72 9 48 65
10
4 44 85 74 29 90 11 38 90 46
10
27 34 79 20 95 3 21 70 28 10
10
64 55 89 90 63 3 49 5 74 89
10
54 21 92 42 82 18 1 71 7 5
10
82 47 85 70 17 59 83 86 37 96
10
61 46 67 63 26 43 25 72 54 57
10
25 73 10 10 37 48 99 54 26 57
10
45 30 38 23 22 91 97 60 51 78
10
8 68 84 98 69 94 70 85 1 57
10
76 33 63 11 27 5 39 25 23 86
10
97 57 69 15 82 0 2 70 13 87
10
59 95 43 41 2 6 65 47 24 21
10
52 59 6 29 99 0 55 58 59 99
10
79 43 99 59 71 35 87 100 55 81
10
97 14 36 73 67 60 0 33 72 84
10
70 44 100 52 12 33 53 17 47 19
10
80 3 95 47 40 40 20 52 94 48
10
24 7 67 91 79 25 4 21 8 0
10
44 42 100 0 59 93 39 51 73 33
10
30 33 15 66 10 68 12 79 9 56
10
71 44 55 4 1 80 60 30 81 63
10
66 45 13 22 86 77 13 59 9 3
10
40 98 86 55 29 74 30 38 79 15
10
14 67 81 2 37 72 46 90 26 6
10
30 9 87 60 16 20 22 35 64 100
10
59 3 18 47 17 67 93 56 82 83
10
46 0 81 74 26 78 46 96 40 61
10
90 93 54 63 30 8 37 61 3 88
10
8 82 60 35 43 31 41 43 45 38
10
95 43 23 7 60 68 35 92 49 84
10
32 61 85 35 95 44 61 77 30 84
10
19 61 49 67 70 74 34 50 66 78
10
53 95 33 62 16 12 61 59 1 96
10
59 31 65 25 90 100 19 16 89 26
10
44 67 33 20 77 48 12 32 88 38
10
76 31 35 96 7 20 22 6 92 76


ouput:

241
336
356
236
266
291
359
219
295
358
227
354
371
299
359
311
278
261
348
196
359
270
394
322
321
363
374
374
313
279
238
289
270
334
330
306
315
296
299
288
250
239
284
307
266
410
254
360
293
252
213
305
278
280
364
308
373
343
315
344
298
300
277
301
298
281
354
304
408
300
266
312
402
291
405
225
315
430
347
282
329
191
321
302
299
227
306
263
272
312
362
323
229
362
373
330
324
322
254
286

"""
