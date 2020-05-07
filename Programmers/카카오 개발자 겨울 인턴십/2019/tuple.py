def solution(s):
    answer = []

    inArray = False

    number = ""
    result = dict()
    for idx, token in enumerate(s):
        if idx != 0 and token == "{":
            inArray = True
            continue
        if inArray:
            if token == "}":
                inArray = False
                # sample_tuple.append()
                if int(number) not in result.keys():
                    result[int(number)] = 0
                result[int(number)] += 1
                number = ""
                # if len(sample_tuple) > len(answer):
                #     answer = sample_tuple
                # sample_tuple = []
            elif token == ",":
                # sample_tuple.append(int(number))
                if int(number) not in result.keys():
                    result[int(number)] = 0
                result[int(number)] += 1
                number = ""
            else:
                number = number + token
    result = sorted(result.items(), key=lambda r : r[1], reverse= True)
    for key in result:
        answer.append(key[0])
    return answer

if __name__ == "__main__":
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
