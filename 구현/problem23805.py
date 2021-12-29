# https://www.acmicpc.net/problem/23805

n = int(input())
for _ in range(n) :
    print('@@@' * n + ' ' * n  + '@' * n)
for _ in range(3 * n) :
    print(('@' * n + ' ' * n) * 2 + '@' * n )
for _ in range(n) :
    print( '@' * n + ' ' * n + '@@@' * n)
    
    