"""
URL : https://practice.geeksforgeeks.org/problems/painting-the-fence3727/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
"""


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
