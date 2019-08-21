from copy import deepcopy

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dust(cur_m):
    global R, C
    for i in range(R):
        for j in range(C):
            if m[i][j] >= 5:
                cnt = 0
                for k in range(4):
                    tmpx, tmpy = i + dx[k], j + dy[k]
                    if 0 <= tmpx < R and 0 <= tmpy < C and m[tmpx][tmpy] != -1:
                        cur_m[tmpx][tmpy] += m[i][j] // 5
                        cnt += 1
                cur_m[i][j] -= (m[i][j] // 5) * cnt
    return cur_m


rcdx = [0, -1, 0, 1]
def air(cur_m):
    global R, C
    x, y = find_idx()
    d = 0
    curx, cury = x, y
    end = 0
    while True:
        tmpx, tmpy = curx + rcdx[d], cury + dy[d]
        if 0 <= tmpx < R and 0 <= tmpy < C:
            if m[tmpx][tmpy] == -1:
                end = 1
                break
            else:
                if (curx, cury) == (x, y):
                    cur_m[tmpx][tmpy] = 0
                else:
                    cur_m[tmpx][tmpy] = m[curx][cury]
            curx, cury = tmpx, tmpy
        else:
            d += 1
        if end:
            break

    d = 0
    curx, cury = x + 1, y
    end = 0
    while True:
        tmpx, tmpy = curx + dx[d], cury + dy[d]
        if 0 <= tmpx < R and 0 <= tmpy < C:
            if m[tmpx][tmpy] == -1:
                end = 1
                break
            else:
                if (curx, cury) == (x + 1, y):
                    cur_m[tmpx][tmpy] = 0
                else:
                    cur_m[tmpx][tmpy] = m[curx][cury]
            curx, cury = tmpx, tmpy
        else:
            d += 1
        if end:
            break
    return cur_m


def find_idx():
    global R, C
    for i in range(R):
        for j in range(C):
            if m[i][j] == -1:
                return i, j


R, C, T = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(R)]

for t in range(T):
    m = dust(deepcopy(m))
    m = air(deepcopy(m))

result = 0
for i in range(R):
    for j in range(C):
        if m[i][j] > 0:
            result += m[i][j]
print(result)