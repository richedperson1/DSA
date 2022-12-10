alphabet = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm',
            14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}


def numberWay(num):
    n = len(num)
    i = 0
    total = 0
    while i < n:
        if num[i] == 0:
            return 0

        total += 1
        local = num[i]
        i += 1
        if i < n and int(local+num[i]) >= 10 and int(local+num[i]) <= 26:
            total += 1
        if i < n and num[i] == 0 and int(local+num[i]) >= 10 and int(local+num[i]) <= 26:
            i += 1

    return total


print(numberWay("221"))
