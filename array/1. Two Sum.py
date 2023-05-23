"""
URL : https://leetcode.com/problems/two-sum/
"""


arr = [2,7,11,15]
arr = [3,2,4]

tar = 7


"""
Time complexity : O(n^2)
Time complexity : O(1)
"""
def bruteForceApproach():
    try:

        num = len(arr)
        for ind,data in enumerate(arr):
            for ind2 in range(ind+1,num):
                if data+arr[ind2]==tar:
                    return [ind,ind2]
        return -1
    
    except Exception as e:
        return e

"""
Time complexity : O(n)
Time complexity : O(n)
"""


def twoSum( arr: list[int], tar: int):
    
    dist = {}
    curr = 0
    for ind,data in enumerate(arr):
        curr = data
        require = tar - curr
        if require in dist:
            return [dist[require],ind]
        
        dist[curr] = ind


if __name__=="__main__":
    print(bruteForceApproach())


