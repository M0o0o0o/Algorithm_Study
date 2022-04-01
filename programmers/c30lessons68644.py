# https://programmers.co.kr/learn/courses/30/lessons/68644


def solution(numbers):
    ans = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            ans.add(numbers[i] + numbers[j])
    return sorted(list(ans))


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
