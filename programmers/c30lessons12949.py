# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    ans = []
    row = 0
    while row < len(arr1):
        buf = []
        for col in range(len(arr2[0])):
            value = 0
            for r in range(len(arr2)):
                value += arr1[row][r] * arr2[r][col]
            buf.append(value)
        ans.append(buf)
        row += 1
    return ans


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],
      [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
