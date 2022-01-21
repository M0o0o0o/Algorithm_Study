# https://www.acmicpc.net/problem/10927

import hashlib
print(hashlib.md5(input().encode()).hexdigest())
