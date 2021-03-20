# https://www.acmicpc.net/problem/10217

import sys 

INF = int(1e9) 
input = sys.stdin.readline

for _ in range(int(input())) : 
    # n : 공항의 수, m : 총 지원비용, k 티켓정보 
    n, m, k = map(int,input().split())
    list = [[] for _ in range(n+1)]

    for _ in range(k) :
        # u : 출방공항, v : 도착공항, c : 비용, d : 시간 
        u, v, c, d = map(int, input().split())
        list[u].append([v,c,d])

    dp = [[INF] * (m+1) for _ in range(n+1)] // 
    dp[1][0] = 0
    for money in range(m+1) :
        for here in range(1, n+1) :
            if dp[here][money] == INF : # 경로가 없는 경우
                continue

            h_dis = dp[here][money] #here 공항에 money 비용으로 가는데 걸리는 시간(진행상황까지는 최소시간이다) 
            
            for there,t_m, t_d in list[here] :
                if money + t_m > m :
                    continue

                dp[there][money+t_m] = min(dp[there][money+t_m], h_dis + t_d)

    ans = min(dp[n])
    print("Poor KCM" if ans == INF else ans)