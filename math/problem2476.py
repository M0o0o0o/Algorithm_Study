# https://www.acmicpc.net/problem/2476

ans = []
for _ in range(int(input())) :
    lst = sorted(list(map(int, input().split())))
    for i in range(len(lst)) :
        if lst.count(lst[i]) == 3 : 
            ans.append(10000 + (lst[i] * 1000))
            break
        elif lst.count(lst[i]) == 2 :
            ans.append(1000 + (lst[i] * 100))
            break
        if i == 2 : ans.append(lst[2] * 100)
        
print(max(ans))
              
    
    