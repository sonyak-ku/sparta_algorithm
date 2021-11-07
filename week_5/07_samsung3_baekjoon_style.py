from itertools import combinations as cb

def get_min_city_chicken_distance(m, city_map):
    # 치킨집위치들, 집들의 위치들 을 알아야 합니다.
    chicken_stores, houses = [], []  # (1,1) 부터 시작이라는데 별로 안중요할 것같음
    min_chicken_distances = [] # 각 조합의 치킨거리들을 담는다

    for r, city_row in enumerate(city_map):
        for c, city in enumerate(city_row):
            if city == 1:
                houses.append((r, c))
            elif city == 2:
                chicken_stores.append((r, c))   # 맵상에 집들과 치킨집들의 정보를 저장한다.


    chicken_store_combination = cb(chicken_stores, m)
    for combi in chicken_store_combination: # 가장 최종 치킨거리가 최소인 치킨집의 조합을 찾는 용도
        chicken_distances = []
        for house in houses:
            house_distances = []
            for chicken_store in combi:  # 조합의 치킨 집 하나씩 띄운다.
                d = abs(house[0] - chicken_store[0]) + abs(house[1] - chicken_store[1]) # 어떤 치킨집과의 거리를 구함
                house_distances.append(d)
            chicken_distances.append(min(house_distances)) # 어떤 집의 치킨 거리를 담는다.
        min_chicken_distances.append(sum(chicken_distances)) # 해당 조합의 도시의 치킨 거리의 최솟값을 담는다.



    return min(min_chicken_distances)

nx, mx = map(int, input().split())
maps = [list(map(int, input().split())) for i in range(nx)]




print(get_min_city_chicken_distance(mx, maps))