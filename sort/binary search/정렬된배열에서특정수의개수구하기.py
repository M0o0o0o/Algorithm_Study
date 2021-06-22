n, num = map(int, input().split())

lst = list(map(int, input().split()))

left, right = -1, -1


def first(start, end):
    global left
    if start > end:
        return

    mid = (start + end) // 2

    if (mid == 0 or num > lst[mid-1]) and lst[mid] == num:
        left = mid
        return
    elif lst[mid] >= num:
        first(start, mid - 1)
    else:
        first(mid + 1, end)


def last(start, end):
    global right
    if start > end:
        return

    mid = (start + end) // 2

    if (mid == (n-1) or lst[mid+1] > num) and lst[mid] == num:
        right = mid
        return
    elif lst[mid] > num:
        last(start, mid - 1)
    else:
        last(mid + 1, end)


first(0, n-1)
last(0, n-1)

if left == -1 and right == -1:
    print(-1)
else:
    print(right - left + 1)
