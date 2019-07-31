for tc in range(1, int(input()) + 1):
    n = int(input())
    m = [list(input()) for _ in range(n)]

    result = 0
    mid = n // 2 + 1
    for i in range(mid):
        ran = 2 * i + 1
        for j in range((n - ran) // 2, (n - ran) // 2 + ran):
            result += int(m[i][j])
    for i in range(n - mid):
        ran = 2 * i + 1
        for j in range((n - ran) // 2, (n - ran) // 2 + ran):
            result += int(m[n - i - 1][j])
    print(f"#{tc} {result}")