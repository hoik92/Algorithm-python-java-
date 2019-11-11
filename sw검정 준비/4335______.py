def dfs(x, y, h, cnt, n, nx, ny):
    global N, result
    if h > result:
        result = h
    if cnt == N:
        return
    if h > memo[n][cnt - 1][nx][ny]:
        memo[n][cnt - 1][nx][ny] = h
    else:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            for j in range(3):
                if m[i][j] <= x:
                    for k in range(3):
                        if j != k and m[i][k] <= y:
                            for l in range(3):
                                if j != l and k != l:
                                    dfs(m[i][j], m[i][k], h + m[i][l], cnt + 1, i, j, k)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    memo = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            memo[i][j] = [[-1] * 3 for _ in range(3)]

    result = 0
    dfs(10000, 10000, 0, 0, 0, 0, 0)
    print("#{} {}".format(tc, result))