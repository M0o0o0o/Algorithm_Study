# https://www.acmicpc.net/problem/2110

n, c = map(int, input().split())

house = []

for _ in range(n):
    house.append(int(input()))
house.sort()

start = 1
end = house[n-1] - house[0]

result = 0

while start <= end:
    mid = (start + end) // 2
    value = house[0]
    count = 1

    for i in range(1, n):
        if (house[i] - value) >= mid:
            value = house[i]
            count += 1

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
