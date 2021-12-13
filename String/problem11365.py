# https://www.acmicpc.net/problem/11365

while True : 
    string = input().strip('\n')
    if string == 'END' : break
    print(string[::-1])