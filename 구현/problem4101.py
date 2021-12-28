# https://www.acmicpc.net/problem/4101

while True :
    a, b = map(int, input().split())
    if a + b == 0 : break
    print('Yes') if a > b else print('No')