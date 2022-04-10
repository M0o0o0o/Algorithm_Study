# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    ans = 0
    visited = {w: False for w in words}
    visited[begin] = True
    q = deque([(begin, 0)])
    ans = 0
    while q:
        current, cnt = q.popleft()
        if current == target:
            ans = cnt
            break
        for word in words:
            if not visited[word]:
                diff = 0
                for i in range(len(word)):
                    if current[i] != word[i]:
                        diff += 1
                    if diff > 2:
                        break
                if diff == 1:
                    visited[word] = True
                    q.append((word, cnt + 1))
    return ans


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(solution("aab", "aba", ["abb", "aba"]))
