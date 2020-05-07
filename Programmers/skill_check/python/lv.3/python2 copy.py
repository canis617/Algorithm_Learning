def func(routes, answer):
    if len(routes) == 0:
        return answer

    start = routes[0][0]
    end = routes[0][1]

    new_list = []
    inRoute = False
    for idx, route in enumerate(routes):
        if idx == 0:
            answer += 1
        else:
            for i in range(route[0], route[1]+1):
                if i >= start and i <= end:
                    inRoute = True
                    break
            if not inRoute:
                new_list.append(route)
            inRoute = False
    answer = func(new_list, answer)
    return answer

def func2(routes, answer):
    if len(routes) == 0:
        return answer

    start = [-30001]
    end = [30001]
    max_start = max(start)
    min_end = min(end)
    for route in routes:
        if route[0] < min_end:
            start.append(route[0])
            end.append(route[1])
        else:
            answer += 1
            start = [-30001]
            end = [30001]
        max_start = max(start)
        min_end = min(end)
    answer +=1
    return answer


def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda route: route[0])
    print(routes)
    answer = func2(routes, answer)
    return answer

if __name__ == "__main__":
    print(solution(
        [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
        )
    )

# 결과 : 시간초과
