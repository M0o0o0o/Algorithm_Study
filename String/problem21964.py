# https://www.acmicpc.net/problem/21964

n = int(input())
string = list(input())[::-1]
count, index, ans = 0, 0, ''

while count < 5 :
    if string[index] != ' ' :
        ans += string[index]
        count += 1
    index += 1

print(ans[::-1])