def price_level(price,previous_price):
    if (price - previous_price >= 0.5) or (price - previous_price <= -0.5):
        level = "level-0.5"
    if (price - previous_price >= 1) or (price - previous_price <= -1):
        level = "level-1"
    if (price - previous_price >= 2) or (price - previous_price <= -2):
        level = "level-2"
    if (price - previous_price >= 3) or (price - previous_price <= -3):
        level = "level-3"
    if (price - previous_price >= 4) or (price - previous_price <= -4):
        level = "level-4"
    if (previous_price == 0):
        level = "0"

    if (price > previous_price):
        position = "UP"
    else:
        position = "DOWN"

    return level,position

level,position=price_level(1000.0008,0)

print(level,position)