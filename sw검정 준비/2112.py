from copy import deepcopy

def de_replace(d, ab):
    m[d] = mm[d]


def replace(d, ab):
    global W
    m[d] = [ab] * W


def dfs(cnt, start):
    global D, W, K, result
    if cnt >= result:
        return
    if check():
        if cnt < result:
            result = cnt
        return

    for i in range(start + 1, D):
        if not visited[i]:
            visited[i] = 1
            for j in range(2):
                replace(i, j)
                dfs(cnt + 1, i)
                de_replace(i, j)
            visited[i] = 0


def check():
    global D, W, K
    for i in range(W):
        cnt = 1
        passed = False
        for j in range(D - 1):
            if m[j][i] == m[j + 1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= K:
                passed = True
                break
        if not passed:
            return False
    return True


for tc in range(1, int(input()) + 1):
    D, W, K = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(D)]
    mm = deepcopy(m)
    visited = [0] * D

    result = K
    dfs(0, -1)
    print("#{} {}".format(tc, result))