dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def direction(x, y, d, c):
    global N, M
    if c == 5:
        tmpd = (d + 2) % 4
        tmpx = x + dx[tmpd]
        tmpy = y + dy[tmpd]
        if m[tmpx][tmpy] == 1:
            return tmpx, tmpy, 5
        elif m[tmpx][tmpy] == 2:
            return tmpx, tmpy, d

    tmpd = (d + 1) % 4
    tmpx = x + dx[tmpd]
    tmpy = y + dy[tmpd]
    if 0 < tmpx < N - 1 and 0 < tmpy < M - 1:
        if m[tmpx][tmpy] == 0:
            return tmpx, tmpy, tmpd
    return direction(x, y, tmpd, c + 1)


def dfs(x, y, d):
    global N, M, cnt, end
    if m[x][y] == 0:
        m[x][y] = 2
        cnt += 1

    tmpx, tmpy, tmpd = direction(x, y, d, 1)
    if tmpd == 5:
        return
    dfs(tmpx, tmpy, tmpd)


N, M = map(int, input().split())
x, y, d = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
if d == 1:
    d = 3
elif d == 3:
    d = 1
dfs(x, y, d)

print(cnt)