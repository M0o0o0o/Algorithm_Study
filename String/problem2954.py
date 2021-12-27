# https://www.acmicpc.net/problem/2954

string = list(input())
ans = ''
index = 0 

while index < len(string) :
    ans += string[index]
    if string[index] in ['a','e','i','o','u'] :
        index += 2
    index += 1
print(ans)