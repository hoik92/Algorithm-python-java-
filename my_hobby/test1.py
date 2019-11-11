def solution(bombs):
    bombs.sort()
    # print(bombs)
    answer = 0
    for i in range(len(bombs)):
        if bombs[i] >= i + 1:
            answer += 1
        else:
            break
    print(answer)
    return answer