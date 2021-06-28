# 해당 문제는 '이것이 취업을 위한 코딩 테스트다'에 있는 Flipkart 인터뷰 문제입니다.

# n x m 크기의 금광이 있습니다. 금광은 1 x 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의
# 금이 들어 있습니다. 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다. 맨 처음에는
# 첫번째 열의 어느 행에서든 출발할 수 있습니다. 이후에 m번에 걸쳐서 매번 오른쪽 위, 오른쪽,
# 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다. 결과적으로 채굴자가 얻을 수 있는
# 금의 최대 크기를 출력하는 프로그램을 작성하세요.


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    mine = []
    lst = list(map(int, input().split()))
    index = 0
    for i in range(n):
        mine.append(lst[index:index+m])
        index += m

    result = 0
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                up = 0
            else:
                up = mine[i-1][j-1]
            if i == n-1:
                down = 0
            else:
                down = mine[i+1][j-1]

            mid = mine[i][j-1]

            mine[i][j] += max(up, mid, down)
            result = max(result, mine[i][j])

    print(result)

# 해당 문제는 다이나믹 프로그래밍을 이용한다.
# 특정 dp[i][j]에서 최대값이 되게 하는 과정을 반복함으로써 최대값을 찾을 수 있다.
# dp[i][j] = dp[i][j] + max(dp[i][j-1], dp[i-1][j-1], dp[i+1][j-1])
