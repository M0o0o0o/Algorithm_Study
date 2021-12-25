# https://www.acmicpc.net/problem/1755

lst = ['zero','one','two','three','four','five','six','seven','eight','nine']
s, e = map(int, input().split())
ans = []

for i in range(s, e+1) :
    num = list(str(i))
    numTostr = ''
    for n in num : 
        numTostr += lst[int(n)]
    ans.append((numTostr, i))
    
ans.sort()
for i in range(0,len(ans)) : 
    if (i+1) % 10 == 0 : 
        print(ans[i][1])
    else :
        print(ans[i][1], end = ' ')