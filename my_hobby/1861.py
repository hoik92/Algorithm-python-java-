import sys
sys.setrecursionlimit(10000)

def dfs(x, y, cnt, st):
    global N, result, start, end
    if start == m[x][y]:
        start = st
        result += cnt - 1
        return

    if cnt >= result:
        if cnt > result:
            start = st
            end = m[x][y]
        else:
            if start > st:
                start = st
                end = m[x][y]
        result = cnt

    visited = False
    for i in range(4):
        tmpx, tmpy = x + dx[i], y + dy[i]
        if 0 <= tmpx < N and 0 <= tmpy < N and m[x][y] + 1 == m[tmpx][tmpy]:
            visited = True
            dfs(tmpx, tmpy, cnt + 1, st)
        if visited:
            return


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, int(input()) + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]

    if tc == 7:
        s = 1
    start = N * N + 1
    end = 0
    result = 0
    for i in range(N):
        for j in range(N):
            if not (start <= m[i][j] <= end):
                dfs(i, j, 1, m[i][j])

    print("#{} {} {}".format(tc, start, result))