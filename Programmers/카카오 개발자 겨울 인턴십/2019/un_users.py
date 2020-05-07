def solution(user_id, banned_id):
    answer = 0

    banned=True
    result = list()
    for ban in banned_id:
        ban_count = 0
        banned_list = list()
        for user in user_id:
            if len(user) != len(ban):
                continue
            for u, z in zip(user, ban):
                if z != '*' and u != z:
                    banned = False
            if banned:
                banned_list.append(user)
            banned = True
        result.append((ban ,banned_list))

    banned_list = sorted(result, key = lambda r : len(r[1]))
    
    _, answer = dfs(banned_list, [], [])
    
    for idx, a in enumerate(answer):
        answer[idx] = sorted(answer[idx])
    answer = sorted(answer)

    print(answer)

    tmp = list()
    result = list()
    for idx, a in enumerate(answer):
        if a == tmp:
            continue
        if a != tmp:
            result.append(a)
            tmp = a
    return len(result)

def dfs(banned_list, current_list, result):
    if len(banned_list) == 0:
        result.append(current_list)
        return current_list, result
    selected = banned_list[0]
    for banned_id in selected[1]:
        current_list.append(banned_id)
        new_banned_list = copy.deepcopy(banned_list[1:])
        for b, i in new_banned_list:
            for after_id in i:
                if after_id == banned_id:
                    i.remove(after_id)
                if len(i) == 0:
                    new_banned_list.remove((b, i))
        current_list, result = dfs(new_banned_list, current_list, result)
        current_list = current_list[:-1]
    
    return current_list, result 

import copy
            
if __name__ == "__main__":
    print(solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["*rodo", "*rodo", "******"]
        )
    )
