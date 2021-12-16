# https://www.acmicpc.net/problem/1264

while True :
    string = input() 
    if string == '#' : break
    ans = 0
    for s in string : 
        if s in ['a','e','i','o','u','A','E','I','O','U'] : ans += 1
        
    print(ans)