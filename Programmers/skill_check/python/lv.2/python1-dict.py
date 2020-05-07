def solution(clothes):
    answer = 0

    new_cloths  = dict()
    for cloth in clothes:
        if cloth[1] not in new_cloths.keys():
            new_cloths[cloth[1]] = list()
        new_cloths[cloth[1]].append(cloth[0])

    answer = 1
    for key in new_cloths.keys():
        answer = answer * (len(new_cloths[key]) + 1)
    answer -= 1
    return answer

if __name__ == "__main__":
    print(solution(
        [
            ["yellow_hat", "headgear"],
            ["bluesungloasses", "eyewear"],
            ["green_turban", "headgear"],
        ]
        )
    )