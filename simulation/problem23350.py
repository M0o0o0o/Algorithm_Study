# https://www.acmicpc.net/problem/23350


from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

c, pri = deque(), dict()
ans = 0

for _ in range(n):
    order, weight = map(int, input().split())
    c.append((order, weight))
    if order in pri:
        pri[order] += 1
    else:
        pri[order] = 1

pri = sorted([(key, pri[key]) for key in pri.keys()], key=lambda x: -x[0])

priIdx = 0
while priIdx < len(pri):
    priOrder, priCnt = pri[priIdx]
    cnt, lst = 0, []
    while cnt < priCnt:
        ans += c[0][1]
        if c[0][0] == priOrder:
            cnt += 1
            value = c.popleft()[1]
            i = 1
            if not lst:
                lst.append(value)
                continue
            buf = []

            while lst and lst[-1] < value:
                buf.append(lst.pop())
            if buf:
                ans += sum(buf) * 2
            lst.append(value)

            while buf:
                lst.append(buf.pop())
            continue
        c.append(c.popleft())
    priIdx += 1

print(ans)
