for tc in range(1, int(input())+1):
    N = int(input())
    m = [0] * N
    matrix = [[0] * 10 for _ in range(10)]

    cnt = 0
    for i in range(N):
        m[i] = list(map(int, input().split()))
        for j in range(m[i][0], m[i][2] + 1):
            for k in range(m[i][1], m[i][3] + 1):
                if m[i][4] == 1:
                    if matrix[j][k] == 0:
                        matrix[j][k] = 1
                    elif matrix[j][k] == 2:
                        matrix[j][k] = 3
                        cnt += 1
                elif m[i][4] == 2:
                    if matrix[j][k] == 0:
                        matrix[j][k] = 2
                    elif matrix[j][k] == 1:
                        matrix[j][k] = 3
                        cnt += 1

    print("#{} {}".format(tc, cnt))