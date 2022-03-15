# https://www.acmicpc.net/problem/15781

n, m = map(int, input().split())
print(max(list(map(int, input().split()))) + max(list(map(int, input().split()))))
