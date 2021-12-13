# https://www.acmicpc.net/problem/1159

n = int(input())
alpha = [0] * 26

for _ in range(n) :
    alpha[ord(input().strip('\n')[0]) - 97] += 1

ans = []
for i in range(26) :
    if alpha[i] >= 5 : ans.append(chr(97 + i))


if ans : 
    print("".join(ans))
else : 
    print("PREDAJA")        