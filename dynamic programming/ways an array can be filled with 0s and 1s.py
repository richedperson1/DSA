# Number of ways an array can be filled with 0s and 1s such that no consecutive elements are 1

# url : https://www.geeksforgeeks.org/number-ways-array-can-filled-0s-1s-no-consecutive-elements-1/

# Method 1
"""
Short-Cut Used
1. # : Number 

This method is used when we only need to counts # of way we can fill an array with zero's and ones
we can'nt able to return anything here

"""


def nth_term(n):

    a = 1
    b = 1
    c = 1

    # Construct fibonacci upto
    # (n+2)th term the first
    # two terms being 1 and 1
    for i in range(0, n):
        c = a + b
        a = b
        b = c
    return c


# print(nth_term(3))


# Method 1.1

def n_size_array_fill_1_0(n, ind, pre_one):
    if ind >= n:
        return 1
    ans = 0
    ans += n_size_array_fill_1_0(n, ind+1, False)
    if pre_one == False:
        ans += n_size_array_fill_1_0(n, ind+1, True)

    return ans


for ii in range(1, 10):
    print(n_size_array_fill_1_0(ii, 0, False))
# Method 2
"""
Short-Cut Used
1. # : Number 

This method is used when we need to also return possible outcome's through which array is filled 
with zero's and once's

"""

ans = []  # array ans is in global scope


def numberOfWay(n, i, local):
    """
    This is the base case 
    when i == n then it will add list in ans list
    """
    if i >= n:
        ans.append(local)
        return
    """
    When i = 0 
    We can place zero as well as one in starting  position
    """
    if i == 0:
        numberOfWay(n, i+1, local+[0])
        numberOfWay(n, i+1, local+[1])

    if len(local) >= 1 and local[-1] == 0:
        numberOfWay(n, i+1, local+[1])
        numberOfWay(n, i+1, local+[0])

    if len(local) >= 1 and local[-1] == 1:
        numberOfWay(n, i+1, local+[0])


numberOfWay(3, 0, [])
print(ans)
