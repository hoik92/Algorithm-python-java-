def rotate(i, d):
    visited[i] = 1
    if i != 0:
        if m[i - 1][2] != m[i][6] and not visited[i - 1]:
            rotate(i - 1, -d)
    if i != 3:
        if m[i + 1][6] != m[i][2] and not visited[i + 1]:
            rotate(i + 1, -d)

    if d == 1:
        tmp = m[i].pop()
        m[i].insert(0, tmp)
    elif d == -1:
        tmp = m[i].pop(0)
        m[i].append(tmp)


for tc in range(1, int(input()) + 1):
    K = int(input())
    m = [list(map(int, input().split())) for _ in range(4)]

    for i in range(K):
        idx, dir = map(int, input().split())
        visited = [0] * 4
        rotate(idx - 1, dir)

    result = 0
    for i in range(4):
        if m[i][0]:
            result += 1 << i
    print("#{} {}".format(tc, result))