import math
from itertools import combinations

def min_cost_for_item_type(shops, j, S):
    n = len(shops)
    min_cost = float('inf')
    
    # Single shop cost
    for i in range(n):
        if shops[i][j] > 0:
            cost = math.ceil(S / shops[i][j])
            min_cost = min(min_cost, cost)
    
    # Two-shop combination cost
    for i, i_prime in combinations(range(n), 2):
        if shops[i][j] > 0 and shops[i_prime][j] > 0:
            # Try all possible splits of S between shop i and shop i_prime
            for x in range(S + 1):
                cost_i = math.ceil(x / shops[i][j])
                cost_i_prime = math.ceil((S - x) / shops[i_prime][j])
                total_cost = cost_i + cost_i_prime
                min_cost = min(min_cost, total_cost)
    
    return min_cost

def can_construct_items_of_size(shops, m, S, k):
    total_cost = 0
    for j in range(m):
        cost = min_cost_for_item_type(shops, j, S)
        total_cost += cost
        if total_cost > k:
            return False
    return total_cost <= k

def max_item_size(n, m, shops, k):
    low, high = 1, max(max(row) for row in shops) * k
    best_size = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_construct_items_of_size(shops, m, mid, k):
            best_size = mid
            low = mid + 1
        else:
            high = mid - 1
    return best_size

class Solution:
    def maxSize(self,n,m,shops,k):
        return max_item_size(n,m,shops,k)
    
    
# Example usage:
n = 4
m = 3
shops = [
    [3, 2, 5],
    [1, 3, 2],
    [2, 2, 2],
    [1, 1, 1]]
k = 11
# =================
n = 3
m = 3
shops = [
    [3, 1,5],
    [1,1,2],
    [2,2,2],
    [1, 1, 1]
]
k = 11

print(max_item_size(n, m, shops, k))  # Output: 12
