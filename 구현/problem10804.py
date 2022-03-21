# https://www.acmicpc.net/problem/10804


cards = [i for i in range(21)]
for _ in range(10):
    a, b = map(int, input().split())
    cards = cards[:a] + cards[a:b+1][::-1] + cards[b+1:]
print(*cards[1:])
