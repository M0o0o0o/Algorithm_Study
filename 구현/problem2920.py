# https://www.acmicpc.net/problem/2920

string = list(map(str,input().split()))
string = "".join(string)
if string == '12345678' :
    print('ascending')
elif string == '87654321' :
    print('descending')
else :
    print('mixed')