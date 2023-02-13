
low = 1
high = 99


def countOdds(low: int, high: int) -> int:
    total = 0
    for ind in range(low, high+1):
        if ind & 1 == 1:
            total += 1
    return total


def countOdds2(low: int, high: int) -> int:
    total = (high - low)//2.
    if low & 1 or high & 1:
        total += 1
    return int(total)


total = (high - low)//2


def main(low, high):
    print(countOdds(low, high))
    print(countOdds2(low, high))


main(low, high)
