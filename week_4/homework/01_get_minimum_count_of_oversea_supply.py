import heapq


ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

#재고가 바닥나는 시점 이전까지 받을 수 있는 밀가루중 가장 많이 주는 밀가루를 받는것.
#일고리즘을 풀수있냐 없냐는, 문제의 풀이, 핵심을 짧게 정리할 수 있냐 없냐 에 따라 갈리는 것!!!!!

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):

    sup_count = 0
    date = 1
    heap_supplement = []

    while k-date: #버텨야 하는 날을 전부 버티면 반복문 종료
        # 지난 날에 받을 수 있는 재고들을 리스트에 담아두고
        # 재고가 0 이 되면 해당 리스트에서 받을 수 있는 가장 높은 보급 값을 받아서 보충한다.
        stock -= 1
        if dates: # 리스트가 비었는지 아닌지 체크
            if dates[0] <= date:
                heapq.heappush(heap_supplement, supplies[0] * -1)
                #첫날, 첫날재고 없애고
                del dates[0]
                del supplies[0]

        if stock == 0:
            stock = stock + (heapq.heappop(heap_supplement) * -1)
            sup_count += 1

        date += 1

    return sup_count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))