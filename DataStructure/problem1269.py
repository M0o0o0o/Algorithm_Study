n, m = map(int, input().split())
a, b = set(list(map(int, input().split()))), set(list(map(int, input().split())))

print(len(list(a-b)) + len(list(b-a)))