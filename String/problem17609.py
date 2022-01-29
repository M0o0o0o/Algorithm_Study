# https://www.acmicpc.net/problem/17609

import sys 
input = sys.stdin.readline

def check(word, left, right) :
    while left < right : 
        if word[left] == word[right] : 
            left += 1
            right -= 1
        else : 
            return False
    return True

def ispal(word,left,right ) :
    if word == word[::-1] : 
        return 0
    else :
        while left < right : 
            if word[left] != word[right] : 
                c_left = check(word, left + 1, right)
                c_right = check(word, left, right - 1)
                
                if c_left or c_right : 
                    return 1
                else : 
                    return 2
            else :
                left += 1
                right -= 1
                
for _ in range(int(input())) :
    s = input().strip('\n')
    print(ispal(s, 0, len(s) -1))