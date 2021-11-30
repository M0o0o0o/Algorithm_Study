# https://www.acmicpc.net/problem/18238
import sys; input = sys.stdin.readline

zoac = 'A' + input().strip('\n')
ans = 0
for i in range(1, len(zoac)) :
    one, two = ord(zoac[i]) - ord(zoac[i-1]), ord(zoac[i-1]) - ord(zoac[i])
    one = one + 26 if one < 0 else one 
    two = two + 26 if two < 0 else two
    ans += min(one, two)
    
print(ans)