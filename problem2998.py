# https://www.acmicpc.net/problem/2998

a = input().strip('\n')
a = '0' * (3 - (len(a) % 3)) + a

print(oct(int('0b' + a, 2))[2:])