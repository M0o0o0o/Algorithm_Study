# https://www.acmicpc.net/problem/4613

while True : 
    string = '.' + input()
    string.replace(' ', '')
    if string == '.#' : break
    ans = 0
    for i in range(1, len(string)) :
        if 'A' <= string[i] <= 'Z' :
            ans += i * (ord(string[i]) - 64)
    print(ans)