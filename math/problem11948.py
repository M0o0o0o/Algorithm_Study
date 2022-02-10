# https://www.acmicpc.net/problem/11948

lst = [int(input()) for _ in range(6)]
print(sum(lst) - min(lst[:4]) - min(lst[4:]))