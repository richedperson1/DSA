"""
URL : https://leetcode.com/problems/removing-stars-from-a-string/
"""


def remove_star(string):

    num = len(string)
    ind = 0

    while ind < len(string):
        char = string[ind]
        if char != "*":
            ind += 1
            continue
        if char == "*" and ind-1 >= 0 and string[ind-1] != "*":
            form_str = string[ind-1]+"*"
            string = string.replace(form_str, "", 1)
            ind -= 1

        else:
            local = ind
            while local < len(string) and string[local] == "*":
                local += 1

            while string and local-1 >= 0 and string[local-1] == "*" and string[local] != "*":
                string = string[:local-1]+string[local+1:]

        # ind += 1
    return string if string != "" else 123


final = "a**bbb*c"
final = "*ab*"
final = """"""
print(remove_star(final))
