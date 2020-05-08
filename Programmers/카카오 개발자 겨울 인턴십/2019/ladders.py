def solution(stones, k):
    answer = 0
    max_index = max(stones)
    distance = dict()
    for i in range(1, max_index+1):
        max_distance = 0
        tmp = i
        for s in stones:
            if s < i:
                count += 1
                max_distance = max(count, max_distance)
            else:
                count = 0
        distance[i] = max_distance
    
    for key, value in distance.items():
        if value >= k:
            answer = key - 1
            break



    return answer

if __name__ == "__main__":
    print(solution(
        [2, 4, 5, 3, 2, 1, 4, 2, 5, 1],
        # [1,1,1,1,1,1,1,1],
    	3
    ))
# 정확성 반, 효율성 0