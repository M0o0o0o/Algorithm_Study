# https://www.acmicpc.net/problem/5021

import sys
input = sys.stdin.readline
# 나라를 세운 사람과 혈통이 가장 가까운 사람은 그의 자손이 아닌 사람과 피가 덜 섞인 사람이다.
# 나라를 세운 사람의 자식은 1/2 왕족이며, 그 아들이 왕족이 아닌 사람과 결혼한 경우에는 아들의 자식은 1/4 왕족이 된다.

n, m = map(int, input().split())
king = input().strip('\n')
