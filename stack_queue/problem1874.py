# https://www.acmicpc.net/problem/1874


next = 1
lst, answer = [], []
check = True
for _ in range(int(input())) :
    num = int(input())
    while num >= next :
        lst.append(next)
        answer.append('+')
        next += 1
    if lst and num == lst[-1] :
        answer.append('-')
        lst.pop()
        continue
    check = False
    break

if not check : 
    print('NO')
else :
    for i in answer :
        print(i)
    

