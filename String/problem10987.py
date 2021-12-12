# https://www.acmicpc.net/problem/10987

string = list(input().strip('\n'))
ans = 0

for s in string : 
    if s in ['a','e','i','o','u'] : ans += 1
    
print(ans)