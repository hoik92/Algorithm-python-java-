from itertools import combinations

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def vi(x, y):
    global N, M, tmp, result
    tmp += 1
    if tmp > result:
        return
    for i in range(4):
        tmpx, tmpy = x + dx[i], y + dy[i]
        if 0 <= tmpx < N and 0 <= tmpy < M and m[tmpx][tmpy] == 0 and not visited[tmpx][tmpy]:
            visited[tmpx][tmpy] = 1
            vi(tmpx, tmpy)


N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
com = []
virus = []
pill = 0
for i in range(N):
    for j in range(M):
        if m[i][j] == 0:
            com.append((i, j))
        elif m[i][j] == 1:
            pill += 1
        elif m[i][j] == 2:
            virus.append((i, j))
A = combinations(com, 3)
result = N * M
tmp = 0
for i in A:
    for j in range(3):
        x, y = i[j]
        m[x][y] = 1
    tmp = 0
    visited = [[0] * M for _ in range(N)]
    for x, y in virus:
        vi(x, y)
    if tmp < result:
        result = tmp
    for j in range(3):
        x, y = i[j]
        m[x][y] = 0

print(N * M - result - pill - 3)