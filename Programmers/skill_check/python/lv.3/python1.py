def sumMoney(n, money, count):
    sumMoney = 0
    for price, count in zip(money, count):
        sumMoney += (price * count)
    return sumMoney

def func(n, money, idx, count, answer):
    if idx == len(money):
        return answer
    
    if sumMoney(n, money, count) < n:
        count[idx] += 1
        answer = func(n, money, idx, count, answer)
    if sumMoney(n, money, count) == n:
        answer += 1
    if sumMoney(n, money, count) >= n:
        while(count[idx] != 0):
            count[idx] -= 1
            answer = func(n, money, idx+1, count, answer)
    return answer

def solution(n, money):
    answer = 0
    count = []
    rev_money = []
    for idx, m in enumerate(money):
        rev_money.append( money[len(money)-idx-1] )
        count.append(0)
    answer = func(n, rev_money, 0, count, answer)
    answer = (answer % 1000000007)
    return answer

if __name__ == "__main__":
    print(solution(
        5, [1,2,5]
        )
    )

# 결과 : 시간초과
