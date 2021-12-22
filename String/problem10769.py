# https://www.acmicpc.net/problem/10769


string = input()
h = string.count(":-)")
s = string.count(":-(")
if h > s:
    print('happy')
elif h < s:
    print('sad')
elif h == 0 and s == 0:
    print('none')
else:
    print('unsure')
