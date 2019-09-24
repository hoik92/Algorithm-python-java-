from copy import deepcopy

def dfs(cnt, mm, result):
    global W, H, N, ans
    if cnt == N:
        if result < ans:
            ans = result
        return

    for i in range(W):
        h = choice(i, mm)
        if h == -1:
            continue
        tmpm = bomb(i, h, mm[h][i], deepcopy(mm), cnt)
        result = state(tmpm)
        dfs(cnt + 1, deepcopy(tmpm), result)


def choice(w, mmm):
    for i in range(H):
        if mmm[i][w] != 0:
            return i
    return -1


def bomb(w, h, k, mmmm, cnt):
    global W, H
    mmmm[h][w] = 0
    for i in range(4):
        tmpw, tmph = w, h
        for j in range(k - 1):
            tmpw += dw[i]
            tmph += dh[i]
            if 0 <= tmpw < W and 0 <= tmph < H:
                if mmmm[tmph][tmpw] > 1:
                    mmmm = bomb(tmpw, tmph, mmmm[tmph][tmpw], mmmm, cnt)
                mmmm[tmph][tmpw] = 0
            else:
                break
    return mmmm


def state(mmmmm):
    cnt = 0
    for i in range(W):
        pad = []
        for j in range(H):
            c = mmmmm[H - 1 - j][i]
            if c != 0:
                pad.append(c)
                cnt += 1
        for j in range(H):
            if pad:
                mmmmm[H - 1 - j][i] = pad.pop(0)
            else:
                mmmmm[H - 1 - j][i] = 0
    return cnt


dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]
for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(H)]

    ans = W * H
    debug = 0
    dfs(0, deepcopy(m), ans)
    if ans == W * H:
        ans = 0
    print("#{} {}".format(tc, ans))