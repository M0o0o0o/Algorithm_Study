# 고정점이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미한다.
# 하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있다
# 이때 이 수열에소 고정점이 있으면, 고정점을 출력하는 프로그램을 작성하세요. 고정점은 최대 1개만 존재한다.
# 만약 고정점이 없으면 -1을 출력한다.


def binary(lst, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if lst[mid] == mid:
        return mid

    elif lst[mid] < mid:
        return binary(lst, mid + 1, end)
    else:
        return binary(lst, start, mid-1)


n = int(input())
lst = list(map(int, input().split()))

print(binary(lst, 0, n-1))
