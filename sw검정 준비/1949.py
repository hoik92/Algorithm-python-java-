def go(x, y, h, cur):
    global N, K, can, result
    if cur > result:
        result = cur

    for i in range(4):
        tmpx, tmpy = x + dx[i], y + dy[i]
        if 0 <= tmpx < N and 0 <= tmpy < N and not visited[tmpx][tmpy]:
            if h <= m[tmpx][tmpy] and can:
                visited[tmpx][tmpy] = 1
                can = False
                for j in range(1, K + 1):
                    if m[tmpx][tmpy] - j < h:
                        go(tmpx, tmpy, m[tmpx][tmpy] - j, cur + 1)
                        break
                visited[tmpx][tmpy] = 0
                can = True
            elif h > m[tmpx][tmpy]:
                visited[tmpx][tmpy] = 1
                go(tmpx, tmpy, m[tmpx][tmpy], cur + 1)
                visited[tmpx][tmpy] = 0


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    max_height = m[0][0]
    start = []
    for i in range(N):
        for j in range(N):
            if m[i][j] == max_height:
                start.append((i, j))
            elif m[i][j] > max_height:
                max_height = m[i][j]
                start = [(i, j)]

    result = 1
    can = True
    for x, y in start:
        visited[x][y] = 1
        go(x, y, m[x][y], 1)
        visited[x][y] = 0
    print("#{} {}".format(tc, result))