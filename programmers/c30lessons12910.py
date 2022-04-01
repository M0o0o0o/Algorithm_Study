#  https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    ans = []
    for a in arr:
        if a % divisor == 0:
            ans.append(a)

    return sorted(ans) if ans else [-1]


print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))
