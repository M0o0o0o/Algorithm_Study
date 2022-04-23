# https://www.acmicpc.net/problem/5575

import sys
from datetime import datetime
input = sys.stdin.readline


for _ in range(3):
    lst = list(input().split())
    cal = str(datetime.strptime(':'.join(
        lst[3:]), '%H:%M:%S')-datetime.strptime(':'.join(lst[:3]), '%H:%M:%S'))
    cal = cal.replace('00', '0')
    cal = cal.split(':')
    cal = [c.lstrip('0') if len(c) > 1 else c for c in cal]
    print(*cal)
