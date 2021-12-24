# https://www.acmicpc.net/problem/7785

n = int(input())
lst = []
dic = {}
for  _ in range(n) :
    name, log = input().split()
    if name not in dic :
        lst.append(name)
    dic[name] = log
ans = []        
for n in lst : 
    if dic[n] == 'enter' : 
        ans.append(n) 
        
ans.sort(reverse=True)
for a in ans : 
    print(a)       