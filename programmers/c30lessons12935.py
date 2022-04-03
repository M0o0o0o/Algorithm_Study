# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    if len(arr) <= 1:
        return [-1]
    minIdx = arr.index(min(arr))
    return arr[:minIdx] + arr[minIdx+1:]


print(solution([4, 3, 2, 1]))
