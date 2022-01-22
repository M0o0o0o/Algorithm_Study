# https://www.acmicpc.net/problem/3181

ignore = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
lst = list(input().split(' '))
ans = ''
for i in range(len(lst)) :
    if lst[i] not in ignore or i == 0  : 
        ans += lst[i][0].upper()
        
print(ans)