# https://programmers.co.kr/learn/courses/30/lessons/17677

# 두 집합 a,b 사이의
# 자카드 유사도는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값을 정의

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    dic1, dic2 = {}, {}
    for i in range(1, len(str1)):
        if not str1[i-1:i+1].isalpha():
            continue
        if str1[i-1:i+1] in dic1:
            dic1[str1[i-1:i+1]] += 1
            continue
        dic1[str1[i-1:i+1]] = 1

    for i in range(1, len(str2)):
        if not str2[i-1:i+1].isalpha():
            continue
        if str2[i-1:i+1] in dic2:
            dic2[str2[i-1:i+1]] += 1
        else:
            dic2[str2[i-1:i+1]] = 1

    intersec, union = 0, 0
    check = set()

    for key in dic1.keys():
        if key in check:
            continue
        check.add(key)
        if key not in dic2:
            union += dic1[key]
            continue

        intersec += min(dic1[key], dic2[key])
        union += max(dic1[key], dic2[key])
    for key in dic2.keys():
        if key in check:
            continue
        check.add(key)
        union += dic2[key]
    try:
        return int((intersec / union) * 65536)
    except:
        return 65536


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
