from copy import deepcopy

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def pill(cnt, mm, vv):
    global N, M, v
    if cnt == 3:
        vm = deepcopy(mm)
        for x, y in xy:
            virus(x, y, vm, deepcopy(visited))
        cur_v = 0
        for i in range(N):
            for j in range(M):
                if vm[i][j] == 2:
                    cur_v += 1
        if cur_v < v:
            v = cur_v
            # print(vm)
        # print(v)
        return

    for i in range(N):
        for j in range(M):
            if mm[i][j] == 0 and not vv[i][j]:
                mm[i][j] = 1
                vv[i][j] = 1
                pill(cnt + 1, mm, deepcopy(vv))
                mm[i][j] = 0


def virus(x, y, mmm, vvv):
    global N, M, v
    vvv[x][y] = 1
    mmm[x][y] = 2
    # print(mmm)
    for i in range(4):
        tmpx, tmpy = x + dx[i], y + dy[i]
        if 0 <= tmpx < N and 0 <= tmpy < M and mmm[tmpx][tmpy] == 0 and not vvv[tmpx][tmpy]:
            virus(tmpx, tmpy, mmm, vvv)


N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
v = N * M
visited = [[0] * M for _ in range(N)]

xy = []
for i in range(N):
    for j in range(M):
        if m[i][j] == 2:
            xy.append((i, j))

pill(0, deepcopy(m), deepcopy(visited))

pill_cnt = 0
for i in range(N):
    for j in range(M):
        if m[i][j] == 1:
            pill_cnt += 1
ans = N * M - v - pill_cnt
print(ans - 3)