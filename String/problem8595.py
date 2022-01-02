# https://www.acmicpc.net/problem/8595

n = int(input())
s = input() + 'Z'

result = 0
hidden_num = ''
for i in range(len(s)):
    if s[i].isdigit() and len(hidden_num) < 6:
        hidden_num += s[i]
    elif s[i].isalpha() and hidden_num:
        result += int(hidden_num)
        hidden_num = ''

print(result)