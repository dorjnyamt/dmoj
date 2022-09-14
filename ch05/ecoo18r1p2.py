for dataset in range(10):
    n_routes = int(input())
    routes = []
    for i in range(n_routes):
        route = list(map(int, input().split()))
        routes.append(route[0:1] + route[2:])

    routes.sort(key=lambda route_id: route_id[0])
    bottleneck = min([min(route[1:]) for route in routes])
    bottleneck_routes = []
    for route in range(len(routes)):
        if min(routes[route][1:]) == bottleneck:
            bottleneck_routes.append(route + 1)
    bottleneck_routes.sort()
    print(f"{bottleneck} {{{str(bottleneck_routes).strip('[]').replace(' ', '')}}}")