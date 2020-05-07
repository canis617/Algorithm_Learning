
import sys
sys.setrecursionlimit(100000)
def solution(k, room_number):
    answer = []
    
    total_rooms = dict()
    for r in room_number:
        answer.append(find_room_number(r, total_rooms))
    
    return answer

def find_room_number(r, total_rooms):
    if r not in total_rooms.keys():
        total_rooms[r] = r + 1
        return r
    else:
        next_room = total_rooms[r]
        next_room = find_room_number(next_room, total_rooms)
        total_rooms[r] = next_room + 1
        return next_room

if __name__ == "__main__":
    alist = [i+1 for i in range(100000)]
    alist.append(1)
    print(solution(
        10000000,
        alist
    ))

# result : [1,3,4,2,5,6]
# 시간 초과
