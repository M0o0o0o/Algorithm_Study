# https://www.acmicpc.net/problem/11098

for _ in range(int(input())) :
    lst = []
    for _ in range(int(input())) :
        a, b = input().split()
        lst.append((int(a), b))
    lst.sort()
    print(lst[-1][1])
    