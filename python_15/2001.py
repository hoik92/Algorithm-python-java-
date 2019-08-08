for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N - M + 1):
        tmp = 0
        for j in range(N - M + 1):
            if j == 0:
                for k in range(M):
                    for l in range(M):
                        tmp += m[i + k][l]
            else:
                for k in range(M):
                    tmp -= m[i + k][j - 1]
                    tmp += m[i + k][j - 1 + M]
            if tmp > result:
                result = tmp
    print(f"#{tc} {result}")