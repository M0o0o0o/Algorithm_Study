# https://www.acmicpc.net/problem/2693

for _ in range(int(input())) :
    lst = list(map(int,input().split()))
    print(sorted(lst)[7])