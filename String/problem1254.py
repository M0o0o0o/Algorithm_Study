# https://www.acmicpc.net/problem/1254

s=input()
for i in range(len(s)):
    if s[i:]==s[i:][::-1]:
        print(len(s)+i)
        break