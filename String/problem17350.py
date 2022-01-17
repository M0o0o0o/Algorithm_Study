# https://www.acmicpc.net/problem/17350

ans = '?'
for _ in range(int(input())):
    if input() == 'anj':
        ans = ';'
        break

print('뭐야'+ans)
