def calculate_total(orders):
    total = 0
    for order in orders:
        total += order["value"]
    return total