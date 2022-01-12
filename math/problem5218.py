# https://www.acmicpc.net/problem/5218

for _ in range(int(input())):
    left, right = input().split(' ')
    left, right = list(left), list(right)
    print('Distances:', end=' ')
    for i in range(len(left)):
        if(left[i] <= right[i]):
            print(ord(right[i]) - ord(left[i]), end=' ')
        else:  # left가 크고 right 가 작다
            print((ord('Z') - ord(left[i])) +
                  (ord(right[i]) - ord('A') + 1), end=' ')
    print()
