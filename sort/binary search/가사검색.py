# https://programmers.co.kr/learn/courses/30/lessons/60060
# 노래 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는 지 찾는다.
# 와일드 카드 '?'는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정한다.
# 가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열 queries

# 고려 사항 : 문자 길이, 와일드 카드의 위치, 문자 검색, 이진 탐색
def solution(words, queries):
    answer = []
    words.sort()
    words_length = []
    for i in range(words):
        words_length.append(len(words[i]))

    # 검색의 기준이 와일드 카드와 문자가 골고루 섞인 유형과
    # 모든 문자가 와일드 카드로만 구성된 것도 생각해서 구현해야 한다.
    for i in range(len(queries)):
        query = queries[i]
        query_length = len(query)
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

solution(words, queries)
