# https://programmers.co.kr/learn/courses/30/lessons/12906


def solution(arr):
    newArr = []
    arr.append(11)
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            newArr.append(arr[i-1])
    return newArr


print(solution([1, 1, 3, 3, 0, 1, 1]))
