# https://www.acmicpc.net/problem/1302

n = int(input())
dic = {}

for _ in range(n) :
    book = input()
    if book not in dic : 
        dic[book] = 1
    else :
        dic[book] += 1

lst = []
for i in dic : 
    lst.append((dic[i], i))

lst.sort(reverse=True)

answer = [lst[0][1]]

for i in range(1, len(lst)) :
    if lst[i-1][0] == lst[i][0] :
        answer.append(lst[i][1])
        continue

    break

answer.sort()

print(answer[0])