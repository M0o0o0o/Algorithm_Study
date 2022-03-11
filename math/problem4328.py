# https://www.acmicpc.net/problem/4328

while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    b, p, m = lst[0], lst[1], lst[2]
    n = int(str(p), b) % int(str(m), b)
    ans = []
    while n >= b:
        ans.append(str(n % b))
        n = n//b
    ans.append(str(n))
    print(int(''.join(ans[::-1])))
