# https://programmers.co.kr/learn/courses/30/lessons/42888

# 닉네임을 변결하는 경우
# - 채팅방을 나간 후, 새로운 닉네임을 다시 들억나다.
# - 채팅방에서 닉네임을 변경ㄹ한다.

# """
#     ["Enter uid1234 Muzi",  -> 무지님이 들어왔습니다. -> 프로도님이 들어왔습니다.
#     "Enter uid4567 Prodo" -> 프로도님이 들어왔습니다.
#     ,"Leave uid1234" -> 무지님이 나갔습니다.
#     ,"Enter uid1234 Prodo" -> 프로고님이 들어왔습니다.
#     ,"Change uid4567 Ryan"]
#     """

def makeMessage(nickTracker, record):
    r = list(record.split(' '))
    if r[0] == 'Enter':
        return nickTracker[r[1]] + "님이 들어왔습니다."
    elif r[0] == 'Leave':
        return nickTracker[r[1]] + "님이 나갔습니다."


def solution(record):
    nickTracker = {}
    newRecord = []
    for r in record:
        R = list(r.split(' '))
        if len(R) >= 3:
            nickTracker[R[1]] = R[2]
        if r[0] in ['E', 'L']:
            newRecord.append(r)
    return [makeMessage(nickTracker, r) for r in newRecord]


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
