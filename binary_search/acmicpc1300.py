# https://www.acmicpc.net/problem/1300

n = int(input())
k = int(input())

start, end = 1, k 

while start <= end :
    # mid : ?번째 값을 나타낸다.
    # count : mid번째 값보다 작은 값의 개수를 나타낸다. 
    mid = (start + end) // 2
    count = 0

    for i in range(1, n+1) :
        count += min(mid // i, n)

    if count < k :
        start = mid + 1
    else :
        end = mid - 1

print(start)


# i번째 행의 최댓값은 i * n이다. 따라서 i번째 행에서 m보다 작은 값의 개수는 
# m//i나 n이 된다.
