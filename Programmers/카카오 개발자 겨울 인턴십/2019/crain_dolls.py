def solution(board, moves):
    answer = 0
    stack = dict()
    for idx in range(len(board[0])):
        stack[idx+1] = list()
    for bo in board:
        for idx, b in enumerate(bo):
            if b != 0:
                stack[idx+1].append(b)

    basket = list()
    for m in moves:
        if len(stack[m]) > 0:
            grap = stack[m][0]
            stack[m] = stack[m][1:]
            if len(basket) > 0 and basket[len(basket)-1] == grap:
                basket = basket[:-1]
                answer += 2
            else:
                basket.append(grap)
            
    return answer

if __name__ == "__main__":
    print(solution(
        [
            [0,0,0,0,0],
            [0,0,1,0,3],
            [0,2,5,0,1],
            [4,2,4,4,2],
            [3,5,1,3,1]
        ],
        [1,5,3,5,1,2,1,4]
        )
    )