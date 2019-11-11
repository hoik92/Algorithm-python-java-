for tc in range(1, int(input()) + 1):
    n, a, b = map(int, input().split())
    m = [[-1] * (b + 1) for _ in range(n + 1)]
    m[0][0] = 1
    for i in range(n + 1):
        for j in range(min(i, b) + 1):
            if j == 0 or j == i:
                m[i][j] = 1
            else:
                m[i][j] = m[i - 1][j - 1] + m[i - 1][j]
    print("#{} {}".format(tc, m[n][b]))