# https://www.acmicpc.net/problem/1049

n, m = map(int, input().split())
six, one, ans = [], [], 0
for _ in range(m) :
    a, b= map(int ,input().split())
    six.append(a)
    one.append(b)

if n // 6 > 0 :
    ans += min(((n // 6) * min(six), min(one) * (n // 6) * 6))
if n % 6 > 0 :
    ans += min((n % 6) * min(one), min(six))
print(ans)