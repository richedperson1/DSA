def maxConcatenatedStrings(arr, k):

    size = len(arr)
    def backtrack(index,local):
        if index>=size:
            return 0
        if len(local)>=k:
            return 1
        
        ans = 0
        ans+= backtrack(index+1,local)
        for ind in range(index,size):
            for char in arr[ind]:
                local.add(char)
                
            ans+= backtrack(ind+1,local)


        return ans


    return backtrack(0,set())

# Test cases
n1 = 4
str1 = ["abc", "de", "fg", "h"]
k1 = 11
print(maxConcatenatedStrings(str1, k1))  # Output: 3

n2 = 3
str2 = ["abcde", "de", "fghi"]
k2 = 5
print(maxConcatenatedStrings(str2, k2))  # Output: 2
