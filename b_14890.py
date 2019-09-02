def can(x, y, d, r0c1):
    global N, L
    if r0c1 == 0:
        for i in range(L):
            if 0 <= y + i * d < N and m[x][y + i * d] == m[x][y] and not install[y + i * d]:
                pass
            else:
                return False
        return True
    else:
        for i in range(L):
            if 0 <= x + i * d < N and m[x + i * d][y] == m[x][y] and not install[x + i * d]:
                pass
            else:
                return False
        return True


N, L = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    install = [0] * N
    ans = True
    for j in range(N - 1):
        if m[i][j] - m[i][j + 1] == 0:
            pass
        elif m[i][j] - m[i][j + 1] == 1:
            if can(i, j + 1, 1, 0):
                for k in range(L):
                    install[j + 1 + k] = 1
            else:
                ans = False
                break
        elif m[i][j] - m[i][j + 1] == -1:
            if can(i, j, -1, 0):
                for k in range(L):
                    install[j - k] = 1
            else:
                ans = False
                break
        else:
            ans = False
            break
    if ans:
        result += 1

for i in range(N):
    install = [0] * N
    ans = True
    for j in range(N - 1):
        if m[j][i] - m[j + 1][i] == 0:
            pass
        elif m[j][i] - m[j + 1][i] == 1:
            if can(j + 1, i, 1, 1):
                for k in range(L):
                    install[j + 1 + k] = 1
            else:
                ans = False
                break
        elif m[j][i] - m[j + 1][i] == -1:
            if can(j, i, -1, 1):
                for k in range(L):
                    install[j - k] = 1
            else:
                ans = False
                break
        else:
            ans = False
            break
    if ans:
        result += 1
print(result)