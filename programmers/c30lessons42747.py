# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    ans = 0
    citations.sort()
    

# 나의 h는 어떻게 구할 수 있을까?
# 우측의 표와 같이 자신이 저널에 등재한 전체 논문중 많이 인용된 순으로 정렬한 후,
# 피인용수가 논문수와 같아지거나 피인용수가 논문수보다 작아지기 시작하는 숫자가 바로 나의 h가 됩니다.
