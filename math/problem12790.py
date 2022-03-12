# https://www.acmicpc.net/problem/12790

for _ in range(int(input())):
    hp, mp, st, ar, hpp, mpp, stp, arp = map(int, input().split())
    hp, mp, st, ar = hp + hpp, mp + mpp, st + stp, ar + arp
    hp = hp if hp >= 1 else 1
    mp = mp if mp >= 1 else 1
    st = st if st > 0 else 0
    print(1 * (hp) + 5 * (mp) + 2 * (st) + 2 * (ar))
