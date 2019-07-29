for tc in range(1, int(input()) + 1):
    n = int(input())
    m = [[] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                m[i].append(1)
            elif i > 0:
                m[i].append(m[i - 1][j] + m[i - 1][j - 1])

    print(f"#{tc}")
    for i in m:
        for j in i:
            print(j, end=' ')
        print()