# https://www.acmicpc.net/problem/13234

dic = {'true': True, 'false': False}
l, m, r = input().split(' ')
if m == 'AND' and (dic[l] and dic[r]):
    print('true')
    exit(0)
elif m == 'OR' and (dic[l] or dic[r]):
    print('true')
    exit(0)
print('false')
