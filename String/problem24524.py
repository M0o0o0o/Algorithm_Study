# https://www.acmicpc.net/problem/24524

# T 역시 모든 문자가 다르다
# S의 문자들을 골라내서 T를 만든다.
# 모든 문자가 다르다는게 힌트다!!

S, T = input().strip('\n'), input().strip('\n')
dic = {T[i]: [i, 0] for i in range(len(T))}

for s in S:
    if s not in dic:
        continue

    sIdx = dic[s][0]
    if sIdx == 0:

        dic[s][1] += 1
        continue

    prevChar = T[sIdx - 1]
    if dic[prevChar][1] >= 1:
        dic[s][1] += 1
        dic[prevChar][1] -= 1

print(dic[T[-1]][1])
