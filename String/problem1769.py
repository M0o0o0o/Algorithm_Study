# https://www.acmicpc.net/problem/1769

number, count = input(), 0
while True : 
    if len(number) == 1 :
        print(count)
        if int(number) % 3 == 0 : print('YES')
        else : print('NO')
        break
    
    count += 1
    buf = 0
    for n in number : 
        buf += int(n)
    number = str(buf)