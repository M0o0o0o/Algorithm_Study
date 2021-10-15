# https://www.acmicpc.net/problem/2822

lst = []
for i in range(8) :
    lst.append((int(input()),i+1))

lst.sort(reverse=True)
answer, total = [], 0

for i in range(5) :
    total += lst[i][0]
    answer.append(lst[i][1])

answer.sort()

print(total)
for a in answer :
    print(a, end = ' ')