# https://www.acmicpc.net/problem/1436
# 종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수를 말한다.
# 제일 작은 종말의 숫자는 666이고, 그 다음으로 큰 수는 1666,2666,3666..과
# 같다. 

n = int(input())

six = 666
index = 1 
while True : 
    if n == 1 : 
        print(six) 
        break
    six += 1 
    buf = six
    count = 0 
    while buf > 0 :
        temp = buf % 10
        if temp == 6 :
            count += 1
        elif count < 3 :
            count = 0
        buf //= 10
        
    if count >= 3 : 
        index += 1
        if index == n : 
            print(six)
            break;
        