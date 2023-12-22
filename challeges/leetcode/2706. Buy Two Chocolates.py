def buyChoco( arr: list[int], money: int) -> int:
    first=second = float("inf")

    for data in arr:
        if data<=first:
            second = first
            first = data
        elif data<second and data>first:
            second = data
    
    total = first+second
    if total<=money:
        return money- total
    return money


prices = [41,1,28,2,92,97,1,87]

money = 68
# print(buyChoco(prices,money))

def checking(n):
    assert n==1

