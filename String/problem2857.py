# https://www.acmicpc.net/problem/2857
ans = []
for i in range(1, 6):
    if input().find('FBI') >= 0:
        ans.append(i)

if ans:
    for a in ans:
        print(a, end=' ')
else:
    print('HE GOT AWAY!')
