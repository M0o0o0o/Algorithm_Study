# https://www.acmicpc.net/problem/16987
# 계란은 무게와 내구도가 있다.

# 1. 가장 왼쪽의 계란을 든다.
# 2. 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다. 단, 손에 든 계란이 깨졌거나 깨지지 않은
# 다른 계란이 없으면 치지 않고 넘어간다. 이후 손에 든 계란을 원래 자리에 내려놓고 3번 과정을 진행한다.
# 3. 가장 초근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행한다. 단, 가장 최근에 든 계란이
# 가장 오른쪽에 위치한 게란일 경우 계란을 치는 과정을 종료한다.

# 최대 몇 개의 계란을 꺨 수 있는지 알아맞춰보자

# 계란으로 계란을 치게 되면 각 계란의 내구도는 상대 계란의 무게만큼 깎이게 된다.

def dfs(idx, egg):
    global ans
    if idx == n:
        ans = max(ans, egg.count(0))
        return
    buf = egg[::]
    for i in range(n):
        if idx == i:
            continue
        


n = int(input())
# 내구도 무게
arm = [0] * n
wei = [0] * n
ans = 0
for i in range(n):
    arm[i], wei[i] = map(int, input().split())

dfs(0, wei)
