# # https://www.acmicpc.net/problem/2607

import copy

# 비교할 단어의 길이가 -1, 0 , 1인 경우

n = int(input())
words = [input().strip('\n') for _ in range(n)]
result = 0
source = dict()
for w in words[0]:
    if source.get(w):
        source[w] += 1
    else:
        source[w] = 1


for word in words[1:]:
    copySource = copy.deepcopy(source)
    count = 0
    if word == words[0]:
        continue
    for w in word:
        if copySource.get(w) and copySource[w] >= 1:
            copySource[w] -= 1
        else:
            count += 1
    if count <= 1:
        result += 1

print(result)
