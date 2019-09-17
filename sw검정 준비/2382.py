def move(x, y, n, d):
    global N
    tmpx, tmpy = x + dx[d], y + dy[d]
    if tmpx == 0 or tmpx == N - 1 or tmpy == 0 or tmpy == N - 1:
        n = n // 2
        d = change_d(d)
    return [tmpx, tmpy, n, d + 1]


def change_d(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    info = [0] * K
    for i in range(K):
        info[i] = list(map(int, input().split()))

    for i in range(M):
        for j in range(len(info)):
            x, y, n, d = info[j]
            info[j] = move(x, y, n, d - 1)

        remove = []
        for j in range(len(info)):
            sum_list = [info[j]]
            x, y, n, d = info[j]
            for k in range(j + 1, len(info)):
                xx, yy, nn, dd = info[k]
                if x == xx and y == yy and not k in remove:
                    remove.append(k)
                    sum_list.append(info[k])

            sum_n = n
            for k in range(1, len(sum_list)):
                xx, yy, nn, dd = sum_list[k]
                if n < nn:
                    n = nn
                    d = dd
                sum_n += nn
            info[j] = [x, y, sum_n, d]
        remove.sort(reverse=True)
        for j in remove:
            info.pop(j)

    result = 0
    for i in range(len(info)):
        result += info[i][2]
    print("#{} {}".format(tc, result))