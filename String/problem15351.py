# https://www.acmicpc.net/problem/15351

for _ in range(int(input())) :
    ans = 0
    for a in list(input()) :
        if 65 <= ord(a) <= 90 :
           ans += ord(a) - 64
    if ans == 100 : print('PERFECT LIFE') 
    else : print(ans)
    