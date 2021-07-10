# https://www.acmicpc.net/problem/2579
# 계단은 한 번에 한 계단 혹은 두 계단씩 오를 수 있다. 
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 계단은 반드시 밟아야 한다. 


n = int(input())
lst = [] 
dp = [0] * (n+1)
for _ in range(n) :
    lst.append(int(input()))

# 마지막 계단은 반드시 밟아야 하기 때문에 입력받은 리스트를 뒤집어서 처리
lst.reverse()
lst.append(0)


for i in range(n+1) :
    if i == 0 :
        dp[i] = lst[0]
    elif i == 1 :
        dp[i] = lst[0] + lst[1]
    elif i == 2 :
        dp[i] = lst[0] + lst[2]
    else :
        dp[i] = max(lst[i] + dp[i-2], lst[i] + lst[i-1] + dp[i-3])

print(max(dp[n], dp[n-1]))