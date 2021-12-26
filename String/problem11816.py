# https://www.acmicpc.net/problem/11816

number = input()
if number[0] == '0':
    if number[1] == 'x':
        print(int(number, 16))
    else:
        print(int(number, 8))
else:
    print(int(number))
