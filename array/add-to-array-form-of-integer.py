"""
URL : https://leetcode.com/problems/add-to-array-form-of-integer/solutions/

"""
from typing import *


def addToArrayForm(num: List[int], k: int) -> List[int]:
    first = 0
    n = len(num)
    for ind, data in enumerate(num):
        first = first*10+int(data)

    form = str(first+k)
    num = []
    for ind, data in enumerate(form):
        num.append(int(data))

    return num


def addToArrayForm2(num: List[int], k: int):
    n = len(num)-1
    ele = 0
    for ind in range(n, -1, -1):
        k, num[ind] = divmod(num[ind]+k, 10)

    while k:
        k, a = divmod(k, 10)
        num = [a]+num

    return num


print(addToArrayForm2([1, 9, 9], 32))
