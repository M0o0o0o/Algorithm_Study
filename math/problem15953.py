# https://www.acmicpc.net/problem/15953
A = [0] + [500] + [300] * 2 + [200] * 3 + [50] * 4 + [30] * 5 + [10] * 6 + [0] * 100
B = [0] + [512] + [256] * 2 + [128] * 4 + [64] * 8 + [32] * 16 + [0] * 100
for _ in range(int(input())) :
    a, b = map(int, input().split())
    print((A[a] + B[b]) * 10000)