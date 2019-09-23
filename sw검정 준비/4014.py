def can_install(x, y, d):
    global N, X
    tmp = m[x][y]
    for i in range(X):
        tmpx, tmpy = x + i * dx[d], y + i * dy[d]
        if tmpx < 0 or tmpx >= N or tmpy < 0 or tmpy >= N or installed[tmpx][tmpy] or m[tmpx][tmpy] != tmp:
            return False
    return True


def install(x, y, d):
    global N, X
    for i in range(X):
        tmpx, tmpy = x + i * dx[d], y + i * dy[d]
        installed[tmpx][tmpy] = 1


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    installed = [[0] * N for _ in range(N)]

    cnt = 0
    for i in range(N):
        # installed = [0] * N
        result = True
        for j in range(N - 1):
            if m[i][j] == m[i][j + 1]:
                continue
            elif m[i][j] - m[i][j + 1] == 1:
                if can_install(i, j + 1, 0):
                    install(i, j + 1, 0)
                else:
                    result = False
                    break
            elif m[i][j] - m[i][j + 1] == -1:
                if can_install(i, j, 2):
                    install(i, j, 2)
                else:
                    result = False
                    break
            else:
                result = False
                break
        if result:
            cnt += 1

    installed = [[0] * N for _ in range(N)]
    for i in range(N):
        result = True
        for j in range(N - 1):
            if m[j][i] == m[j + 1][i]:
                continue
            elif m[j][i] - m[j + 1][i] == 1:
                if can_install(j + 1, i, 1):
                    install(j + 1, i, 1)
                else:
                    result = False
                    break
            elif m[j][i] - m[j + 1][i] == -1:
                if can_install(j, i, 3):
                    install(j, i, 3)
                else:
                    result = False
                    break
            else:
                result = False
                break
        if result:
            cnt += 1
    print("#{} {}".format(tc, cnt))