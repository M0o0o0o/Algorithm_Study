# https://www.acmicpc.net/problem/2587

lst = []
for _ in range(5) :
    lst.append(int(input()))
    
print(sum(lst) // 5)
print(sorted(lst)[2])