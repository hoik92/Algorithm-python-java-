m = [[0] * 4001 for _ in range(4001)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    N = int(input())
    q = []
    for i in range(N):
        y, x, d, k = map(int, input().split())
        x = -x * 2 + 2000
        y = y * 2 + 2000
        m[x][y] = k
        q.append([x, y, d, k])

    result = 0
    while q:
        rxy = []
        remove = []
        for i in range(len(q)):
            tx, ty, td, tk = q[i]
            m[tx][ty] -= tk
            tx += dx[td]
            ty += dy[td]
            if 0 <= tx < 4001 and 0 <= ty < 4001:
                if m[tx][ty] and not [tx, ty] in rxy:
                    rxy.append([tx, ty])
                m[tx][ty] += tk
            else:
                remove.append(i)
            q[i] = [tx, ty, td, tk]
        for rx, ry in rxy:
            result += m[rx][ry]
            m[rx][ry] = 0
            for i in range(len(q)):
                if q[i][0] == rx and q[i][1] == ry:
                    remove.append(i)
        remove.sort(reverse=True)
        # print(remove)
        for r in remove:
            q.pop(r)

    print("#{} {}".format(tc, result))