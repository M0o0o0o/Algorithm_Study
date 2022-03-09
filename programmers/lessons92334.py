# https://programmers.co.kr/learn/courses/30/lessons/92334


# 각 유저가 여러 명의 다른 사용자들을 신고
# 각 유저는 k번 이상 다른 유저에게 신고를 당하면 신고처리가 되고
# 신고 처리 당한 유저를 신고한 유저들에게 알림을 줘야한다
# 각 유저들이 알림을 받는 총 회수를 리스트로 리턴해야 한다.

def solution(id_list, report, k):
    users = {id: set() for id in id_list}
    answer = {id: 0 for id in id_list}

    for r in report:
        a, b = r.split(' ')
        users[b].add(a)

    for user in users:
        if len(users[user]) >= k:
            for reporter in list(users[user]):
                answer[reporter] += 1

    return [answer[reporter] for reporter in answer.keys()]


solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo",
         "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)
