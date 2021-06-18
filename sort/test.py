from functools import cmp_to_key

lst = [15, 61, 89, 1, 84, 3, 4, 8641, 3, 515]


def compare(one, two):
    if one > two:
        return 1
    else:
        return -1


print(sorted(lst, key=cmp_to_key(compare)))
