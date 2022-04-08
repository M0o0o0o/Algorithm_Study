# https://www.acmicpc.net/problem/1551

import copy

n, m = map(int, input().split())
lst = list(input().split(','))
ans = copy.deepcopy(lst)
for _ in range(m):
    lst = copy.deepcopy(ans)
    ans = []
    for i in range(1, len(lst)):
        ans.append(str(int(lst[i]) - int(lst[i-1])))

print(','.join(ans))
