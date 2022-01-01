# https://www.acmicpc.net/problem/11383

n, m = map(int, input().split())
ans = 'Eyfa'
before, after = [], []
for _ in range(n) :
    before.append(input())
for _ in range(n) :
    after.append(input())
    
for i in range(n) :
    string = ''
    for b in before[i] :
        string += b * 2
    if string != after[i] : 
        ans = 'Not Eyfa'
        break
print(ans)