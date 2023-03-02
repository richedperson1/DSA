"""
URL : https://leetcode.com/problems/string-compression/description/
"""
from typing import List


def compress(chars: list[str]) -> int:
    walker, runner = 0, 0
    while runner < len(chars):
        count = 1
        chars[walker] = chars[runner]
        while runner+1 < len(chars) and chars[runner] == chars[runner+1]:
            count += 1
            runner += 1

        if count > 1:
            for num in str(count):
                walker += 1
                chars[walker] = num

        walker += 1
        runner += 1

    return walker


"""
Using for loop 
"""


def compressFor(chars: List[str]) -> int:
    chars += " "  # use a dummy char to take care last char
    start = 0
    compress_end = 0
    for i in range(len(chars)):
        if chars[i] != chars[start]:  # only take action when new char starts
            chars[compress_end] = chars[start]
            compress_end += 1
            count = i - start
            if count > 1:
                for k in str(count):
                    chars[compress_end] = k
                    compress_end += 1
            start = i
    return compress_end
