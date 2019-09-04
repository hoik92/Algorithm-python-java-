def dfs(x, y, d, d_x, d_y, cnt):
    global N, result, max_result
    if d == 3 and (x, y) == (d_x, d_y):
        if cnt > result:
            result = cnt
        return
    if max_result < result:
        return

    tmpx, tmpy = x + dx[d], y + dy[d]
    if 0 <= tmpx < N and 0 <= tmpy < N and (not menu[m[tmpx][tmpy]] or (tmpx, tmpy) == (d_x, d_y)):
        menu[m[tmpx][tmpy]] += 1
        dfs(tmpx, tmpy, d, d_x, d_y, cnt + 1)
        menu[m[tmpx][tmpy]] -= 1

    if (x, y) != (d_x, d_y):
        tmpx, tmpy = x + dx[(d + 1) % 4], y + dy[(d + 1) % 4]
        if 0 <= tmpx < N and 0 <= tmpy < N and (not menu[m[tmpx][tmpy]] or (tmpx, tmpy) == (d_x, d_y)):
            menu[m[tmpx][tmpy]] += 1
            dfs(tmpx, tmpy, (d + 1) % 4, d_x, d_y, cnt + 1)
            menu[m[tmpx][tmpy]] -= 1


dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
for tc in range(1, int(input()) + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    menu = [0] * 101
    for i in range(N - 2):
        max_result = (N - i - 1) * 2 + 1
        for j in range(1, N - 1):
            menu[m[i][j]] += 1
            dfs(i, j, 0, i, j, 1)
            menu[m[i][j]] -= 1
    print("#{} {}".format(tc, result - 1))