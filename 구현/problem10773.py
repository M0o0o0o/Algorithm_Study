# https://www.acmicpc.net/problem/10773

k = int(input())
lst = [] 
for _ in range(k) :
    money = int(input())
    if money == 0 :
        lst.pop()
        continue
    lst.append(money)
print(sum(lst))
