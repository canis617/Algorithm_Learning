def solution(k, room_number):
    answer = []
    
    current_room = dict()
    for r in room_number:
        key = r
        while key <= k:
            if key not in current_room.keys():
                current_room[key] = True
                break
            else:
                key += 1
        answer.append(key)

    return answer

if __name__ == "__main__":
    print(solution(
        10,	
        [1,3,4,1,3,1]
    ))

# result : [1,3,4,2,5,6]
# 시간 초과
