# https://programmers.co.kr/learn/courses/30/lessons/60060
# 노래 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는 지 찾는다.
# 와일드 카드 '?'는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정한다.
# 가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열 queries

# 고려 사항 : 문자 길이, 와일드 카드의 위치, 문자 검색, 이진 탐색

from bisect import bisect_left, bisect_right


def count_by_range(str, left_value, right_value):
    left = bisect_left(str, left_value)
    right = bisect_right(str, right_value)
    return right - left


array = [[] for _ in range(10001)]
reversed = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []

    for word in words:
        array[len(word)].append(word)
        reversed[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed[i].sort()

    for query in queries:
        if query[0] == '?':
            result = count_by_range(reversed[len(
                query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
        else:
            result = count_by_range(array[len(query)], query.replace(
                '?', 'a'), query.replace('?', 'z'))

        answer.append(result)

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], [
      "fro??", "????o", "fr???", "fro???", "pro?"]))
