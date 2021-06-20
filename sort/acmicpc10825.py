# https://www.acmicpc.net/problem/10825


n = int(input())
lst = []

for _ in range(n):
    name, kor, eng, math = input().split()
    lst.append([name, int(kor), int(eng), int(math)])

new_lst = sorted(lst, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(new_lst[i][0])

