# https://www.acmicpc.net/problem/1517
import sys 
input = sys.stdin.readline

def mergeSort(start, end) :
    global cnt
    if start < end : 
        mid = (start + end) // 2
        mergeSort(start, mid)
        mergeSort(mid + 1, end)
        
        a = start
        b = mid + 1
        buf = []
        while a <= mid and b <= end :
            if lst[a] <= lst[b] : 
                buf.append(lst[a])
                a += 1
            else : 
                buf.append(lst[b])
                b += 1
                cnt += (mid - a + 1)
        if a <= mid : 
            buf += lst[a:mid + 1]
        if b <= end :
            buf += lst[b:end + 1]
            
        for i in range(len(buf)) : 
            lst[start + i] = buf[i]

n = int(input())
lst = list(map(int, input().split()))
cnt = 0
mergeSort(0, n-1)
print(cnt)