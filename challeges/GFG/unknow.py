def max_score(arr):
    n = len(arr)
    score = 0
    while arr:
        
        # total_score = max(total_score, score)
        
        if arr[0] < arr[-1]:
            score += arr[-1] * n + min(arr)
            arr.pop()
        else:
            score += arr[0] * n + min(arr)
            arr.pop(0)

        n -= 1
        
    
    return score

# Test cases
arr1 = [1, 2]
print("Output for [1, 2]:", max_score(arr1))

arr2 = [2, 3, 4]
print("Output for [2, 3, 4]:", max_score(arr2))
