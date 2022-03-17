# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    ans, dic = [], {}
    for chunk in s[1:len(s)-1].split("},"):
        chunk = chunk.replace('}', '')
        lst = []
        for c in chunk[1:].split(","):
            lst.append(int(c))
        dic[len(lst)] = lst
    for key in sorted(dic.keys()):
        for value in dic[key]:
            if value not in ans:
                ans.append(value)

    return ans


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print('==========')
print(solution("{{20,111},{111}}"))
