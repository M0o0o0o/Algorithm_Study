# https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    stages.append(1000000)
    stages.sort()
    answer = {i: 0 for i in range(1, N+1)}
    count = 1

    for i in range(1, len(stages)):
        if stages[i-1] == stages[i]:
            count += 1
            continue

        if stages[i-1] in answer:
            answer[stages[i-1]] = count / (count + (len(stages) - 1 - i))
            count = 1

    return [num[1] for num in sorted([(answer[k], k)
                                      for k in answer.keys()], key=lambda x: (-x[0], x[1]))]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
