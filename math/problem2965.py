# https://www.acmicpc.net/problem/2965

lst = sorted(list(map(int, input().split())))
print(max(abs(lst[0] - lst[1]),abs(lst[1] - lst[2])) -1)