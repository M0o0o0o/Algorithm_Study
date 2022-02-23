# https://www.acmicpc.net/problem/2355

def sum_(num):
    return (num * (num + 1)) // 2


a, b = map(int, input().split())
print(sum_(b) - sum_(a) - a)
