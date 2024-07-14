def longest_beautiful_subarray(arr):
    n = len(arr)
    prefix_xor = [0] * (n + 1)
    xor_map = {}
    max_len = 0

    # Compute the prefix XOR array
    for i in range(1, n + 1):
        prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]

    # Iterate through the prefix XOR array
    for i in range(n + 1):
        current_xor = prefix_xor[i]
        
        if current_xor in xor_map:
            # If this prefix XOR has been seen before, calculate the length of the subarray
            max_len = max(max_len, i - xor_map[current_xor])
        else:
            # Store the first occurrence of the prefix XOR
            xor_map[current_xor] = i

    return max_len

# Example usage
arr = [14, 2, 5, 7, 9]
n = len(arr)
print("The length of the longest beautiful subarray is:", longest_beautiful_subarray(arr))
