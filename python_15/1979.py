for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for i in range(n):
        cnt_x, cnt_y = 0, 0
        for j in range(n):
            if m[i][j]:
                cnt_x += 1
            else:
                if cnt_x == k:
                    result += 1
                cnt_x = 0
            if m[j][i]:
                cnt_y += 1
            else:
                if cnt_y == k:
                    result += 1
                cnt_y = 0
        if cnt_x == k:
            result += 1
        if cnt_y == k:
            result += 1
    print(f"#{tc} {result}")