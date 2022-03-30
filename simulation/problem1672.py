# https://www.acmicpc.net/problem/1672

n = int(input())
dna = list(input().strip('\n'))
board = {'AA': 'A', 'AG': 'C', 'AC': 'A', 'AT': 'G', 'GA': "C", "GG": 'G', 'GC': 'T', 'GT': 'A',
         'CA': 'A', 'CG': 'T', 'CC': 'C', 'CT': 'G', 'TA': 'G', 'TG': 'A', 'TC': 'G', 'TT': 'T'}
length = len(dna)
while length > 1:
    dna[length-2] = board[dna[length-2] + dna[length-1]]
    length -= 1
print(dna[0])
