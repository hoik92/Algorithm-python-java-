for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]

    loca = []
    for i in range(N):
        for j in range(N):
            if m[i][j]:
                loca.append([i, j])

    if N % 2:
        max_iter = N
    else:
        max_iter = N + 1

    result = 1
    for i in range(2, max_iter + 1):
        pos = i * i + (i - 1) * (i - 1)
        if pos > M * len(loca):
            break
        for j in range(N):
            for k in range(N):
                cnt = 0
                for x, y in loca:
                    dis = abs(x - j) + abs(y - k)
                    if dis < i:
                        cnt += 1
                ans = cnt * M - pos
                if ans >= 0 and cnt > result:
                    result = cnt
    print("#{} {}".format(tc, result))