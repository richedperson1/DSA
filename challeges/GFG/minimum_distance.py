def minDist( x1 : int, x2 : int, x3 : int) -> int:
    # code here
    
    low = min(x1,x2,x3)
    high = max(x1,x2,x3)
    
    
    ans = float("inf")
    for mid in range(low,high+1):
        
        localMaxi = abs(x1-mid)+abs(x2-mid)+abs(x3-mid)
        ans = min(ans,localMaxi)
        # if localMaxi<ans:
        #     ans = localMaxi
    return ans





def min_total_distance(x1, x2, x3):
    return max(x1,x2,x3)-min(x1,x2,x3)

# Example usage:
# Example usage:
x1 = 15
x2 = 16
x3 = 10

result = min_total_distance(x1, x2, x3)
print(f"{result}")

print(mini_dist(x1,x2,x3))