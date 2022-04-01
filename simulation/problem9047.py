# # https://www.acmicpc.net/problem/9047

for _ in range(int(input())):
    num = int(input())
    cnt = 0
    while num != 6174:
        # 큰 수 작은 수 만들기
        lst = sorted(list(str(num)))
        num = int(''.join(lst[::-1])) - int(''.join(lst))
        cnt += 1
        if num < 1000:
            sNum = str(num)
            for _ in range(4 - len(sNum)):
                sNum += '0'
            num = int(sNum)

    print(cnt)
