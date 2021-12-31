# https://www.acmicpc.net/problem/5704

while True : 
    alpha = [0] * 26
    string = list(input())
    if string[0] == '*' : break
    for s in string :
        if 0 <= ord(s) - 97 <= 26 : 
            alpha[ord(s) - 97] += 1
    if alpha.count(0) > 0 : 
        print('N')
    else : print('Y')

            