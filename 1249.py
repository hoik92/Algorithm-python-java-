def dfs(x, y, cnt):
    global N, end_x, end_y
    if (x, y) == (end_x, end_y):
        if memo[x][y] > cnt:
            memo[x][y] = cnt
        return

    if cnt > memo[end_x][end_y]:
        return

    if memo[x][y] > cnt:
        memo[x][y] = cnt
    else:
        return

    for i in range(4):
        tmpx = x + dx[i]
        tmpy = y + dy[i]
        if 0 <= tmpx < N and 0 <= tmpy < N and not visited[tmpx][tmpy] and memo[tmpx][tmpy] > cnt + int(m[tmpx][tmpy]):
            visited[tmpx][tmpy] = 1
            dfs(tmpx, tmpy, cnt + int(m[tmpx][tmpy]))
            visited[tmpx][tmpy] = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, int(input()) + 1):
    N = int(input())
    m = [list(input()) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    memo = [[90000] * N for _ in range(N)]

    start_x, start_y = 0, 0
    end_x, end_y = N - 1, N - 1

    visited[0][0] = 1
    dfs(start_x, start_y, 0)

    print("#{} {}".format(tc, memo[N - 1][N - 1]))