"""
URL : https://practice.geeksforgeeks.org/problems/painting-the-fence3727/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
"""


def countWay2(n, k):
    if n <= 2:
        return n

    final = (countWay2(n-1, k)+countWay2(n-2, k))*(k-1)
    return final % (10**9+7)


"""
Time complexity : O(n)
space complexity : O(1)
"""


def paintFenceOptimize(n, k):

    similar, different = 0, k
    total = k
    for i in range(2, n):
        similar = different
        different = total*(k-1)
        total = similar+different

    return total


print(paintFenceOptimize(5, 3))
print(countWay2(5, 3))
