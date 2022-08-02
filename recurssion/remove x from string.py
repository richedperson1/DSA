"""
Given a string, compute recursively a new string where all 'x' chars have been removed.

Sample Input 1 :
xaxb
Sample Output 1:
ab


Sample Input 2 :
abc
Sample Output 2:
abc


Sample Input 3 :
xx
Sample Output 3:

"""
st = ["xaxb", "abc", "xx"]


def remove_ele(string, x):
    if len(string) == 0:
        return ""
    small = remove_ele(string[1:], x)

    if string[0] != x:
        return string[0]+small
    else:
        return small


# for i in st:
#     print(remove_ele(i, "x"))


"""
remove pi from the string and replace with 3.14 value

input 1 :
asbpi
output 1 :
asb3.14

"""

# Approach 1


def change_pi(string):
    if len(string) == 1:
        return string
    small = change_pi(string[1:])
    if string[0] == 'p' and string[1] == 'i':
        small = small[1:]
        return "3.14"+small
    else:
        return string[0]+small

# Approach 2


def change_pi_2(string):
    if len(string) <= 1:
        return string

    if string[0] == 'p' and string[1] == 'i':
        small = change_pi_2(string[2:])
        return "3.14"+small
    else:
        small = change_pi_2(string[1:])
        return string[0]+small


string = "pi-->pi"
print(string[-2:])
print(change_pi(string))
print(change_pi_2(string))
