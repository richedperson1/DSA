"""
URL : https://leetcode.com/problems/verifying-an-alien-dictionary/

"""

words = ["word", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"


def checking(w1, w2, dist):
    i, j = 0, 0
    while i < len(w1) and j < len(w2):

        if dist[w1[i]] > dist[w2[j]]:
            return False
        if dist[w1[i]] < dist[w2[j]]:
            return True
        i += 1
        j += 1

    return len(w1) <= len(w2)


def alienDist(word, order):
    dist = {" ": 0}
    for ind, letter in enumerate(order):
        dist[letter] = ind+1

    num = len(word)
    for i in range(num-1):
        if not(checking(word[i], word[i+1], dist)):
            return False

    return True


def alienDict(word, order):
    largeWord = len(max(word))

    dist = {" ": 0}
    for ind, letter in enumerate(order):
        dist[letter] = ind+1

    arrSize = len(word)
    ind = 0
    while ind < arrSize:
        for col in range(1, arrSize):
            if len(word[col-1]) <= ind:
                pastLeter = " "
            else:
                pastLeter = word[col-1][ind]

            if len(word[col]) <= ind:
                currLetter = " "
            else:
                currLetter = word[col][ind]

            if currLetter != pastLeter and dist[pastLeter] < dist[currLetter]:
                print(pastLeter, currLetter)
                return True
            if dist[pastLeter] > dist[currLetter]:
                return False

    return True


print(alienDist(words, order))
