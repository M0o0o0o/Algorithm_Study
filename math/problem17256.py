# https://www.acmicpc.net/problem/17256

ax, ay, az = map(int, input().split()) 
zx, zy, zz = map(int, input().split()) 
print(zx - az, zy // ay, zz - ax)
