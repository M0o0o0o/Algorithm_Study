# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    return [[arr1[r][c] + arr2[r][c] for c in range(len(arr1[0]))]for r in range(len(arr1))]
