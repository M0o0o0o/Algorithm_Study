# https://www.acmicpc.net/problem/15726

a, b, c = map(int, input().split())
ans = max((a*b)/c,a*(b/c), (a/b)*c,a/(b*c))
print(int(ans))
