def get_sum(numbers):
    sum_num = 0
    for number in numbers:
        sum_num += number
    return sum_num
    
def func(numbers, target, idx, answer):
    if idx == len(numbers):
        return answer

    if idx == len(numbers) - 1:
        if get_sum(numbers) == target:
            answer += 1

    answer = func(numbers, target, idx + 1, answer)

    numbers[idx] = numbers[idx] * (-1)

    if idx == len(numbers) - 1:
        if get_sum(numbers) == target:
            answer += 1
    answer = func(numbers, target, idx + 1, answer)

    numbers[idx] = numbers[idx] * (-1)

    return answer
    

def solution(numbers, target):
    answer = 0

    answer = func(numbers, target, 0, answer)

    return answer

if __name__ == "__main__":
    print(solution(
        [1, 1, 1, 1, 1], 3
        )
    )