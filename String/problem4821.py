# https://www.acmicpc.net/problem/4821

import sys
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        exit()
    ans = [0]*(n+1)
    tmp = list(sys.stdin.readline().split(","))
    tmp[-1] = tmp[-1].replace("\n", "")
    cnt = 0
    for i in range(len(tmp)):
        if '-' in tmp[i]:
            a, b = map(int, tmp[i].split('-'))
            if a <= b:
                if a <= n:
                    if b <= n:
                        for j in range(a, b+1):
                            ans[j] = 1
                    else:
                        b = n
                        for j in range(a, b+1):
                            ans[j] = 1
        else:
            if int(tmp[i]) <= n:
                ans[int(tmp[i])] = 1
    print(sum(ans))
