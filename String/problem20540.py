# https://www.acmicpc.net/problem/20540

dic = {'E':"I", 'I':'E', 'S':'N', 'N':'S', 'T':'F', 'F':'T','J':'P', 'P':'J'}
[print(dic[m], end = '') for m in list(input())]