# https://www.acmicpc.net/problem/1620
import sys 
input = sys.stdin.readline

n, m = map(int,input().split())
dic = {} 
for i in range(1, n+1) :
    pocket = input()
    pocket = pocket.strip('\n')
    dic[pocket] = str(i)
    dic[str(i)] = pocket
    
for _ in range(m) :
    pocket = input()
    pocket = pocket.strip('\n')
    print(dic[pocket])


