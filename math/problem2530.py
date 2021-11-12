# https://www.acmicpc.net/problem/2530

h, m, s = map(int , input().split())
d = int(input())

m += d // 60
s += d % 60
if s >= 60 : 
    m += s // 60
    s = s % 60
if m > 59 :
    h += m // 60
    m = m % 60
if h > 23 :
    h = h % 24
    
print(h,m,s)
    