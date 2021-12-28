# https://www.acmicpc.net/problem/5543
B = [int(input()),int(input()),int(input())]
C = [int(input()),int(input())]
ans = int(1e9)
for b in B :
    for c in C :
        ans = min(ans, (b + c) - 50)
print(ans)