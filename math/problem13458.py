# https://www.acmicpc.net/problem/13458

room = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())

result = room
for s in students:
    s -= b
    if s > 0:
        if s % c:
            result += (s // c) + 1
        else:
            result += (s // c)

print(result)
