# https://www.acmicpc.net/problem/2670

n = int(input())
lst = [float(input()) for _ in range(n)]
for i in range(1, n):
    lst[i] = max(lst[i-1] * lst[i], lst[i])
print('%0.3f' % max(lst))
