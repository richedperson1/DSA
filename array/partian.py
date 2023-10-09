def partitionLabels( s: str) -> list[int]:
    ans = []
    dist = {}

    for ind1,char in enumerate(s):
        dist[char] = ind1

    maxi = dist[s[0]]
    start = 0
    end = 0
    for ind,data in enumerate(s):
        maxi = max(maxi,dist[data])
        if maxi> ind:
            maxi = max(maxi,dist[data])
            end = max(maxi,ind)

        elif maxi==ind:
            ans.append(maxi-start+1)
            start = ind+1
        else:
            start = end = ind

    return ans

s = "acda"
print(partitionLabels(s))