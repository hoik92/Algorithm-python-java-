def s():
    global N, n
    tmp1, tmp2 = 0, 0
    for i in range(N):
        for j in range(i + 1, N):
            if visited[i] == 1 and visited[j] == 1:
                tmp1 += m[i][j]
                tmp1 += m[j][i]
            elif visited[i] == 0 and visited[j] == 0:
                tmp2 += m[i][j]
                tmp2 += m[j][i]
    return abs(tmp1 - tmp2)


def dfs(cnt, k):
    global n, N, ans
    if cnt == n:
        tmp_ans = s()
        if tmp_ans < ans:
            ans = tmp_ans
        return
    if cnt + N - k < n:
        return
    for i in range(k, N):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt + 1, i)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    n = N // 2
    visited = [0] * N
    result = [0, 0]
    ans = 20000 * 64
    dfs(0, 0)
    print(f"#{tc} {ans}")
