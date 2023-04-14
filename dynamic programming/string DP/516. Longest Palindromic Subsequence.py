

def longest_sequence(string, start, end):
    if start == end:
        return 1

    if start > end:
        return 0

    if string[start] == string[end]:
        return 2 + longest_sequence(string, start+1, end-1)

    left = longest_sequence(string, start+1, end)
    right = longest_sequence(string, start, end-1)
    return max(left, right)


string = "aabcaa"

print(longest_sequence(string, 0, len(string)-1))
