# https://www.acmicpc.net/problem/2565

# 전깃줄이 전봇대에 연결되는 위치는 위에서부터 차례대로 번호가 매겨진다.
# 전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때,
# 남아있는 모든 전깃줄이 서로 교차하기 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램을 작성하시오.

n = int(input())

lst = []

for _ in range(n) :
    a, b = map(int,input().split())
    lst.append((a,b))

lst.sort()

dp = [1] * n 

for i in range(n) :
    for j in range(i) :
        if lst[j][1] < lst[i][1]:
            dp[i] = max(dp[i], dp[j] + 1) 

print(n - max(dp))