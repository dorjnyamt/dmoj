for dataset in range(10):
    franchises, days = map(int, input().split())
    sales = []
    dozens = 0
    for day in range(days):
        sales.append(list(map(int, input().split())))
        
    for day in sales:
        # print(f"Daily {sum(day)}")
        if sum(day) % 13 == 0:
            dozens += sum(day) // 13

    for franchise in range(franchises):
        franchise_sales = 0
        for day in range(days):
            franchise_sales += sales[day][franchise]
        # print(f"Franchise {franchise_sales}")
        if franchise_sales % 13 == 0:
            dozens += franchise_sales // 13

    print(dozens)