arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = [0] * (len(arr) * 4)

# !! 세그먼트 트리를 배열의 각 구간 합으로 채워주기
# start : 배열의 시작 인덱스, end : 배열의 마지막 인덱스
# index : 세그먼트 트리의 인덱스(1부터 시작)
# 세그먼트 트리의 root 노드의 인덱스를 1부터 시작하는 이유는 2를 곱했을 때 왼쪽 자식 노르를 가리키고
# 2를 곱하고 1을 더하면 오른쪽 자식 노드를 가리키므로 효과적으로 처리하기 위해서다.


def init(start, end, index):
    # print("---start : " , start, "end : ", end , "index : ", index)
    if start == end:  # 가장 끝에 도달햇으면 arr[index] 값 삽입
        # print("!!!!!start == end!!!!!", start, end, index)
        # print('tree[index] = ', arr[start])
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    # 좌측 노드와 우측 노드를 채워주면서 부모 노드의 값을 채워준다.
    tree[index] = init(start, mid, index * 2) + \
        init(mid + 1, end, index * 2 + 1)
    # print('======left node + right node ========== ', index, tree[index])
    return tree[index]

# !! 구간 합을 구하는 함수
# start : 시작 인덱스, end : 마지막 인덱스
# left ~ right : 구간 합을 구하고자 하는 범위
def interval_sum(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        print(start, end, left, right)
        return tree[index]
    mid = (start + end) // 2
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)



# !! 특정 원소의 값을 수정하는 함수
# start : 시작 인덱스. end : 마지막 인덱스
# what : 구간 합을 수정하고자 하는 노드
# value : 수정할 값
def update(start, end, index, what, value):
    if what < start or what > end:
        return
    tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)


init(0, len(arr) - 1, 1)
print(interval_sum(0, len(arr) - 1, 1, 4,7))
# print(interval_sum(0, len(arr) - 1, 1, 0, 2))  # 0부터 2까지의 구간 합 (1 + 2 + 3)
# print(interval_sum(0, len(arr) - 1, 1, 6, 7))  # 0부터 2까지의 구간 합 (7 + 8)

# # arr[0]을 +4만큼 수정
# update(0, len(arr) - 1, 1, 0, 4)
# print(interval_sum(0, len(arr) - 1, 1, 0, 2))   # 0부터 2까지의 구간 합 ((1 + 4) + 2 + 3)

# # arr[9]를 -11만큼 수정
# update(0, len(arr) - 1, 1, 9, -11)
# print(interval_sum(0, len(arr) - 1, 1, 8, 9))   # 8부터 9까지의 구간 합 (9 + (10 - 11))
