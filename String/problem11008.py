# https://www.acmicpc.net/problem/11008

for _ in range(int(input())):
    s, c = input().split(' ')
    count = s.count(c)
    print(count + len(s) - (len(c) * count))
