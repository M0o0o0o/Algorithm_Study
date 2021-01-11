# https://www.acmicpc.net/problem/20362

c, answer_p = input().split()
result = 0
P = []
answer = ''
for _ in range(int(c)):
    P.append(list(input().split()))
    if P[-1][0] == answer_p:
        answer = P[-1][1]
for p in P:
    if answer_p == p[0]:
        break
    if answer == p[1]:
        result += 1

print(result)
