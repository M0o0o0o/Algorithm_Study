# https://www.acmicpc.net/problem/10101

lst = []
count = []
answer = ['','Scalene','Isosceles','Equilateral']
for i in range(3) : lst.append(int(input()))

for i in range(3) :
    count.append(lst.count(lst[i]))

if sum(lst) == 180  :
    print(answer[max(count)])
else :
    print('Error')
