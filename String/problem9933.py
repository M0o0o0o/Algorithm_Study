# https://www.acmicpc.net/problem/9933

n = int(input())
pwds = [input().strip('\n') for _ in range(n)]
dic = dict()

for pwd in pwds:
    dic[pwd] = True

for pwd in pwds:
    if dic.get(pwd[::-1]):
        print(len(pwd), pwd[len(pwd) // 2])
        break
