# https://www.acmicpc.net/problem/21734


for s in input():
    print(s * sum(list(map(int, str(ord(s))))))
