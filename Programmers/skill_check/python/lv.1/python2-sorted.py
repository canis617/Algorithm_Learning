def solution(N, stages):
    answer = []
    
    count = 0
    len_user = 0
    failed = []
    for cur_stage in range(1, N+1):
        for user_stage in stages:
            if user_stage >= cur_stage:
                len_user += 1
            if user_stage == cur_stage:
                count += 1
        print(count, len_user)
        failed_percent = count / len_user
        failed.append((cur_stage, failed_percent))
        len_user = 0
        count = 0
    
    answer = [ans[0] for ans in sorted(failed, key=lambda stage: stage[1], reverse=True)]
    return answer

if __name__ == "__main__":
    print(solution(5, [2,1,2,6,2,4,3,3]))
