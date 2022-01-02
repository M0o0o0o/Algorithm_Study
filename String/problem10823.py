# https://www.acmicpc.net/problem/10823
s = ''
while True :
    try : s += input()
    except : break
print(sum(list(map(int, s.split(','))))) 