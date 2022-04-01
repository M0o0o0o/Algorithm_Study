# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])


print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
print(solution([-1, 0, 1],	[1, 0, -1]))
