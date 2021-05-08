# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다. 
# 입력 조건 : 첫째 줄에 하나의 문자열 S가 주어진다
# 출력 조건 : 첫째 줄에 문제에서 요구하는 정답을 출력한다.


#1
# lst = [0] * 26


# inputStr = input()
# num = 0
# for i in range(len(inputStr)) :
#     if (ord(inputStr[i]) - 65) >= 0 and (ord(inputStr[i]) - 65) <= 25 :
#         lst[ord(inputStr[i]) - 65] = lst[ord(inputStr[i]) - 65] + 1
       
#     else :
#         num = num + int(inputStr[i])

# for i in range(26) :
#     if lst[i] > 0 :
#         for j in range(lst[i]) :
#             print(chr(65 + i), end = '')

# print(num, end= '')


data = input()
result = []
value = 0

for x in data :
    if x.isalpha() :
        result.append(x)
    else :
        value += int(x)

result.sort()

if value != 0 :
    result.append(str(value))

print(''.join(result))