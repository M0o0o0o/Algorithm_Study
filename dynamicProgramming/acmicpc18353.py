# https://www.acmicpc.net/problem/18353
# 병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 한다.
# 또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용한다. 
# 그러면서도 남아있는 병사의 수가 최대가 되도록 하고 싶다. 

# 병사에 대한 정보가 주어졌을 때, 남아있는 병사의 수가 최대가 되도록 하기 위해서 열외해야 하는 병사의 수를 출력하는 프로그램을 작성하시오. 

n = int(input())
lst = list(map(int,input().split()))
dp = [1] * n;


for i in range(n) :
    for j in range(0, i) :
        if lst[j] > lst[i] :
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

# 몇 명을 빼든 내림차순이 되게 만든다. 