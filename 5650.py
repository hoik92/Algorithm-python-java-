dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bansa(k, drt):
    if (k == 1 and drt == 1) or (k == 2 and drt == 3) or (k == 3 and drt == 2) or (k == 4 and drt == 2) or (k == 5 and drt == 2):
        return 0
    elif (k == 1 and drt == 3) or (k == 2 and drt == 2) or (k == 3 and drt == 0) or (k == 4 and drt == 3) or (k == 5 and drt == 3):
        return 1
    elif (k == 1 and drt == 0) or (k == 2 and drt == 0) or (k == 3 and drt == 3) or (k == 4 and drt == 1) or (k == 5 and drt == 0):
        return 2
    elif (k == 1 and drt == 2) or (k == 2 and drt == 1) or (k == 3 and drt == 1) or (k == 4 and drt == 0) or (k == 5 and drt == 1):
        return 3


def go(x, y, drt):
    global N
    count = 0
    tmpx, tmpy = x, y
    while True:
        tmpx += dx[drt]
        tmpy += dy[drt]
        if tmpx < 0 or tmpx >= N or tmpy < 0 or tmpy >= N:
            drt = bansa(5, drt)
            count += 1
            continue
        elif 0 < m[tmpx][tmpy] < 6:
            drt = bansa(m[tmpx][tmpy], drt)
            count += 1
        elif m[tmpx][tmpy] > 5:
            if (tmpx, tmpy) == hole[m[tmpx][tmpy]][0]:
                tmpx, tmpy = hole[m[tmpx][tmpy]][1]
            else:
                tmpx, tmpy = hole[m[tmpx][tmpy]][0]
        if m[tmpx][tmpy] == -1 or (tmpx == x and tmpy == y):
            return count


for tc in range(1, int(input()) + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]

    score = 0
    hole = [[] for _ in range(11)]
    for i in range(N):
        for j in range(N):
            if m[i][j] > 5:
                hole[m[i][j]].append((i, j))
    for i in range(N):
        for j in range(N):
            if m[i][j] == 0:
                for k in range(4):
                    tmp = go(i, j, k)
                    if tmp > score:
                        score = tmp
    print(f"#{tc} {score}")
