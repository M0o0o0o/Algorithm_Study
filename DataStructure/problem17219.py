# https://www.acmicpc.net/problem/17219

n, m = map(int, input().split())
dic = {}

for _ in range(n) :
    url, pwd = input().split()
    dic[url] = pwd
    
for _ in range(m) :
    print(dic[input()])