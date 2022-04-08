# https://www.acmicpc.net/problem/1173

# 해야하는 운동 시간, 최소 맥박, 최대 맥박, 운동시 맥박 증가, 휴식시 맥박 감소
# 5 70 120 25 15
N, m, M, T, R = map(int, input().split())
time, ans, current = 0, 0, m
if M - m < T:
    print(-1)
    exit(0)
while time < N:
    if current + T <= M:
        current += T
        time += 1
    else:
        current = max(current - R, m)
    ans += 1
print(ans)
