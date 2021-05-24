# https://www.acmicpc.net/problem/15686
# 치킨 거리는 집과 가장 가가운 치킨집 사이의 거리이다.
# 각각의 집은 치킨 거리를 가지고 있다. 
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다. 
# 0 : 빈칸 , 1 : 집, 2 : 치킨집 
# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업
# 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램 작성 

from itertools import combinations

n, m = map(int, input().split())

chicken = []
house = []

for row in range(n) :
    data = list(map(int, input().split()))
    for column in  range(n) :
        if data[column]  == 1 :
            house.append((row, column))
        elif data[column] == 2 : 
            chicken.append((row, column))

combi_chicken = list(combinations(chicken,m))

result = int(1e9)

for _chicken in combi_chicken :
    all_street = 0
    for house_r, house_c in house :
        street = int(1e9)
        for _chicken_r, _chicken_c in _chicken :
            street = min(street, abs(house_r - _chicken_r) + abs(house_c - _chicken_c))
        all_street += street
    result = min(result, all_street)

print(result)
