# https://www.acmicpc.net/problem/11179

n = int(input())
print(int('0b' + bin(n)[2:][::-1], 2))
