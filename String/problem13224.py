# https://www.acmicpc.net/problem/13224

ans = 1
for now in list(input()):
    if now == 'A' and ans in [1, 2]:
        ans = 1 if ans == 2 else 2
    elif now == 'B' and ans in [2, 3]:
        ans = 3 if ans == 2 else 2
    elif now == 'C' and ans in [1, 3]:
        ans = 1 if ans == 3 else 3

print(ans)
