def connected(v, drt):
    if drt == 0:
        if v == 1 or v == 4 or v == 5:
            return True
    elif drt == 1:
        if v == 2 or v == 5 or v == 6:
            return True
    elif drt == 2:
        if v == 1 or v == 3 or v == 6:
            return True
    elif drt == 3:
        if v == 2 or v == 3 or v == 4:
            return True
    return False


def dfs(x, y, v, cnt):
    global N, result
    if cnt >= result:
        return
    # if cnt + abs(N - 1 - x) + abs(N - 1 - y) > result:
    if cnt + x + y >= result:
        return
    if (x, y) == (0, 0):
        if 2 in can_go[v]:
            if cnt < result:
                memo[x][y][v] = cnt
                result = cnt
        return
    # if cnt < memo[x][y][v]:
    #     memo[x][y][v] = cnt
    # else:
    #     return

    d = can_go[v]
    for i in d:
        tmpx, tmpy = x + dx[i], y + dy[i]
        if 0 <= tmpx < N and 0 <= tmpy < N and m[tmpx][tmpy] and not visited[tmpx][tmpy]:
            visited[tmpx][tmpy] = 1
            for j in can_rotate[m[tmpx][tmpy]]:
                if connected(j, i):
                    dfs(tmpx, tmpy, j, cnt + 1)
            visited[tmpx][tmpy] = 0


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
can_rotate = [
    0,
    [1, 2],
    [2, 1],
    [3, 4, 5, 6],
    [4, 3, 5, 6],
    [5, 3, 4, 6],
    [6, 3, 4, 5]
]
can_go = [
    0,
    [0, 2],
    [1, 3],
    [0, 1],
    [1, 2],
    [2, 3],
    [0, 3]
]
for tc in range(1, int(input()) + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    memo = [[N * N] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            memo[i][j] = [N * N] * 7

    result = N * N
    # visited[0][0] = 1
    # if m[0][0] == 1:
    #     dfs(0, 0, m[0][0], 1)
    # elif m[0][0] > 2:
    #     dfs(0, 0, 4, 1)
    visited[N - 1][N - 1] = 1
    dfs(N - 1, N - 1, m[N - 1][N - 1], 1)

    print("#{} {}".format(tc, result))