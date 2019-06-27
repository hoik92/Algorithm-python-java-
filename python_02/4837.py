for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    cnt = 0

    for i in range(1 << 12):
        tmp = []
        for j in range(12):
            if i & (1 << j):
                tmp.append(j + 1)
            if len(tmp) > N:
                break
        if len(tmp) == N and sum(tmp) == K:
            cnt += 1
    print("#{} {}".format(tc, cnt))