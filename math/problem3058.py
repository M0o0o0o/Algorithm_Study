# https://www.acmicpc.net/problem/3058

for _ in range(int(input())):
    lst = [l for l in list(map(int, input().split())) if l % 2 == 0]
    print(sum(lst), min(lst))
