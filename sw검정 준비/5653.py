from collections import deque

def activate():
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != 0:
                s.append([i, j, m[i][j][0], m[i][j][0]])


def spread(x, y, v, len_s, cnt):
    for i in range(4):
        tmpx, tmpy = x + dx[i], y + dy[i]
        if m[tmpx][tmpy] == 0:
            m[tmpx][tmpy] = [v, v]
            s.append([tmpx, tmpy, v, v])
        elif m[tmpx][tmpy][1] == m[tmpx][tmpy][0]:
            if m[tmpx][tmpy][0] < v:
                m[tmpx][tmpy] = [v, v]
                idx = -1
                for j in range(len_s - cnt, len(s)):
                    if s[j][0] == tmpx and s[j][1] == tmpy:
                        idx = j
                        break
                if idx != -1:
                    s.remove(s[idx])
                    s.append([tmpx, tmpy, v, v])


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    m = [[0] * (2 * K + M) for _ in range(2 * K + N)]
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(M):
            if tmp[j]:
                m[K + i][K + j] = [tmp[j], tmp[j]]

    s = deque()
    activate()
    for i in range(K):
        cnt = 0
        len_s = len(s)
        for _ in range(len_s):
            cnt += 1
            x, y, v, a = s.popleft()
            if a == 0:
                spread(x, y, v, len_s, cnt)
            if a > -v:
                m[x][y][1] -= 1
                s.append([x, y, v, a - 1])

    ans = 0
    for i in range(len(s)):
        x, y, v, a = s[i]
        if a > -v:
            ans += 1
    print("#{} {}".format(tc, ans))