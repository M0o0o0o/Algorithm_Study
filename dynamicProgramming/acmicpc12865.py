# https://www.acmicpc.net/problem/12865

# 준서가 여행에 필요하다고 생각하는 N개의 무게가 있다.
# 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 하면 준서가 V 만큼 즐길 수 있다.
# 아직 행군을 해본 적이 없는 준서는 최대 K 만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
# 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려 주자.

n, k = map(int, input().split())

stuff = []
dp = []
stuff.append([0,0])
for _ in range(n) :
    weight, value = map(int, input().split())
    stuff.append([weight, value])

dp = [[0]*(k+1) for _ in range(n+1)]

# j만큼의 배낭에 i번째 물건을 담을 수 없다면 이전의 값을 넣고 i=0이라면 0을 대입 
for j in range(1,k+1) :
    for i in range(1,n+1) :
        weight = stuff[i][0]
        value = stuff[i][1]
        if weight <= j :
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])
        else :
            dp[i][j] = dp[i-1][j]


print(dp[n][k])
