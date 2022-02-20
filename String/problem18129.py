# https://www.acmicpc.net/problem/18129

ans = ''
alpha = [False] * 26
string, k = input().split(' ')
string, count, k = string.upper(), 1, int(k)
string += chr(ord(string[-1]) + 1) if string[-1] != 'Z' else 'A'
for i in range(1, len(string)):
    if string[i-1] == string[i]:
        count += 1
        continue
    if not alpha[ord(string[i-1]) - 65]:
        if count >= k:
            ans += '1'
        else:
            ans += '0'
        alpha[ord(string[i-1]) - 65] = True
        count = 1

print(ans)
