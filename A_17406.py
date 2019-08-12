from copy import deepcopy

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def rotate(r, c, s, mat):
    global N, M
    # print(mat)
    start_x, start_y = r - s - 1, c - s - 1
    end_x, end_y = r + s - 1, c + s - 1
    for i in range(s):
        tmp_x, tmp_y = start_x + i, start_y + i
        tmp = mat[tmp_x][tmp_y]
        for j in range(4):
            while True:
                tmp_x += dx[j]
                tmp_y += dy[j]
                tmp, mat[tmp_x][tmp_y] = mat[tmp_x][tmp_y], tmp
                if (tmp_x == start_x + i or tmp_x == end_x - i) and (tmp_y == start_y + i or tmp_y == end_y - i):
                    break
            # print(mat)
    return mat


def find(mat):
    global N, M, result
    for i in range(N):
        tmp = 0
        for j in range(M):
            tmp += mat[i][j]
            if result < tmp:
                break
        if result > tmp:
            result = tmp


def dfs(mat):
    global K
    if sum(visited) == K:
        # print(mat)
        find(mat)
    for i in range(K):
        if not visited[i]:
            r, c, s = k[i][0], k[i][1], k[i][2]
            visited[i] = 1
            tmp_mat = rotate(r, c, s, copy(mat))
            dfs(tmp_mat)
            visited[i] = 0


def copy(mat):
    global N, M
    tmp_m = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            tmp_m[i][j] = mat[i][j]
    return tmp_m


N, M, K = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
k = [list(map(int, input().split())) for _ in range(K)]

result = 100 * M
visited = [0] * K
dfs(m)
# print(m)
print(result)