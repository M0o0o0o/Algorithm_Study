# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    ans = 0
    citations.sort()
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            return len(citations) - idx
    return 0
