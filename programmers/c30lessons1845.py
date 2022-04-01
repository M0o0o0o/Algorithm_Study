# https://programmers.co.kr/learn/courses/30/lessons/1845


def solution(nums):
    setLength = len(set(nums))
    if setLength >= len(nums) // 2:
        return len(nums) // 2
    else:
        return setLength


print(solution([3, 3, 3, 2, 2, 2]))
