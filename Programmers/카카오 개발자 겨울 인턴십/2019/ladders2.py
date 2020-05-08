def solution(stones, k):
    answer = 0
    
    start = 0
    end = max(stones)
    while start <= end:
        if end - start <= 1:
            break
        mid = int((start + end) / 2)
        cur_distance = get_distance(stones, mid)

        if cur_distance <= k:
            start = mid
        elif cur_distance > k:
            end = mid

    return end

def get_distance(stones, pivot):
    temp_stones = stones[:]
    max_count = 0
    count = 1
    for s in temp_stones:
        if s <= pivot:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
    max_count = max(max_count, count)
    return max_count

if __name__ == "__main__":
    print(solution(
        [2, 4, 5, 3, 2, 1, 4, 2, 5, 1],
        # [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        # [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
        # [0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
        # [1,1,3,1,1,1,3,1],
    	3
    ))
# 정확성 반, 효율성 0
