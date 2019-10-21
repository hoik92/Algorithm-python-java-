def dfs(cur_result, cnt):
    global N, result
    if cnt == N:
        if cur_result > result:
            result = cur_result
        return

    for i in range(N):
        if m[cnt][i] and not visited[i]:
            visited[i] = 1
            dfs(cur_result * m[cnt][i], cnt + 1)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    result = 0
    for i in range(N):
        if m[0][i]:
            visited[i] = 1
            dfs(m[0][i], 1)
            visited[i] = 0
    result = (result * 100) / (100 ** N)
    print("#{} {}".format(tc, "%0.6f" % result))