top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    receiver_order = []
    while heights:
        send = heights.pop()
        for tower in heights[::-1]:
            if send < tower:
                receiver_order.append(heights.index(tower) + 1)
                break
        else:
            receiver_order.append(0)

    return receiver_order[::-1]


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!