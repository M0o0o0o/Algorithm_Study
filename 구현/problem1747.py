# https://www.acmicpc.net/problem/1747
n = int(input())
m = 1000001
prime = [False, False] + [True] * (m-2)

for i in range(2, int(m ** 0.5) +1 ) :
    if prime[i] :
        for j in range(i+i, m, i) :
            if prime[j] :
                prime[j] = False

ans = 0
for i in range(n, m) :
    if i == 1 :
        continue
    if str(i) == str(i)[::-1] :
        if prime[i] :
            ans = i
            break

if ans == 0 : ans = 1003001
print(ans)
