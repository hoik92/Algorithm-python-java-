from copy import deepcopy

dx = [0, 0, 0, 0, 0, 0]
dx[1] = [[0], [1], [0], [-1]]
dx[2] = [[0, 0], [1, -1], [0, 0], [1, -1]]
dx[3] = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dx[4] = [[0, -1, 0], [-1, 0, 1], [0, 1, 0], [1, 0, -1]]
dx[5] = [[0, 1, 0, -1] for _ in range(4)]

dy = [0, 0, 0, 0, 0, 0]
dy[1] = [[1], [0], [-1], [0]]
dy[2] = [[1, -1], [0, 0], [1, -1], [0, 0]]
dy[3] = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dy[4] = [[-1, 0, 1], [0, 1, 0], [1, 0, -1], [0, -1, 0]]
dy[5] = [[1, 0, -1, 0] for _ in range(4)]

def dfs(mm, cnt, tmp):
    global N, M, result
    if cnt == len(loc):
        if tmp < result:
            result = tmp
        return
    # if tmp > result:
    #     return
    x, y = loc[cnt]
    for i in range(4):
        tmp2, tmpm = look(x, y, mm[x][y], i, deepcopy(mm), tmp)
        dfs(deepcopy(tmpm), cnt + 1, tmp2)


def look(x, y, val, drt, mmm, tmp):
    global N, M
    for i in range(len(dx[val][drt])):
        tmpx, tmpy = x, y
        while True:
            tmpx += dx[val][drt][i]
            tmpy += dy[val][drt][i]
            if 0 <= tmpx < N and 0 <= tmpy < M and mmm[tmpx][tmpy] == 0:
                mmm[tmpx][tmpy] = '#'
                tmp -= 1
            elif tmpx < 0 or tmpx >= N or tmpy < 0 or tmpy >= M:
                break
            elif m[tmpx][tmpy] == 6:
                break
    return tmp, mmm


N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]

loc = []
result = 0
for i in range(N):
    for j in range(M):
        if 0 < m[i][j] < 6:
            loc.append((i, j))
        elif m[i][j] == 0:
            result += 1

dfs(deepcopy(m), 0, result)
print(result)