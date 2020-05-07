def solution(n):    
    answer = []
    while (n != 0):
        answer.append(n%10)
        n = int(n/10)
    return answer

if __name__ == "__main__":
    print(solution(12345))
