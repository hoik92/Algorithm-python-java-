from collections import deque

def connected(x, y, drt):
    v = m[x][y]
    if drt == 0:
        if v == 1 or v == 3 or v == 6 or v == 7:
            return True
    elif drt == 1:
        if v == 1 or v == 2 or v == 4 or v == 7:
            return True
    elif drt == 2:
        if v == 1 or v == 3 or v == 4 or v == 5:
            return True
    elif drt == 3:
        if v == 1 or v == 2 or v == 5 or v == 6:
            return True
    return False


def can_go(value):
    return direction[value]


def bfs():
    global N, M, L, result

    while q:
        x, y, time = q.popleft()
        if time == L:
            return
        d = can_go(m[x][y])
        for i in d:
            tmpx, tmpy = x + dx[i], y + dy[i]
            if 0 <= tmpx < N and 0 <= tmpy < M and m[tmpx][tmpy] > 0 and not visited[tmpx][tmpy] and connected(tmpx, tmpy, i):
                visited[tmpx][tmpy] = 1
                result += 1
                q.append([tmpx, tmpy, time + 1])


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = [
    0,
    [0, 1, 2, 3],
    [1, 3],
    [0, 2],
    [3, 0],
    [1, 0],
    [2, 1],
    [2, 3]
]
for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    result = 1
    visited[R][C] = 1
    q = deque()
    q.append([R, C, 1])
    bfs()
    print("#{} {}".format(tc, result))