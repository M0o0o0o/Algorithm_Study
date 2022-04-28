# https://www.acmicpc.net/problem/10768
m, d = int(input()), int(input())
if m < 2 or (m == 2 and d < 18):
    print('Before')
elif m == 2 and d == 18:
    print('Special')
else:
    print('After')
