# https://www.acmicpc.net/problem/2576

total, minNum = 0, int(1e9)
for _ in range(7) :
    num = int(input())
    if num % 2 != 0 :
        total += num
        minNum = min(minNum, num)

if total == 0 :
    print(-1)
else :
    print(total)
    print(minNum)