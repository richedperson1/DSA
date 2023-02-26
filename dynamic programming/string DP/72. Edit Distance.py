
w1 = "house"
w2 = "hou"


def distance(w1, w2, ind1, ind2):
    n1, n2 = len(w1), len(w2)

    if ind1 >= n1:
        return max(0, n2-ind2)

    if ind2 >= n2:
        return max(0, n1-ind1)

    if w1[ind1] == w2[ind2]:
        return distance(w1, w2, ind1+1, ind2+1)

    dele = distance(w1, w2, ind1+1, ind2)
    replace = distance(w1, w2, ind1+1, ind2+1)
    insert = distance(w1, w2, ind1, ind2+1)

    return min(dele, replace, insert)+1


print(distance(w1, w2, 0, 0))
