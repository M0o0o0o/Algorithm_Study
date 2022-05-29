# # https://www.acmicpc.net/problem/15719
import sys
n = int(input())
check = [False] * (n+1)

nums = sys.stdin.read()
total, tmp = 0, ''
for num in nums:
    if num.isdigit():
        tmp += num
    elif num == ' ':
        total += int(tmp)
        tmp = ''
total += int(tmp)
print(total - ((n * (n-1)) // 2))
