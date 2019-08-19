dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
def rotate(x, y):
    return -y, x


def gen(x, y, d, g, n):
    dragon = []
    dragon.append([x, y])
    next_endx, next_endy = x + dx[d], y + dy[d]
    dragon.append([next_endx, next_endy])
    m[y][x], m[next_endy][next_endx] = n, n
    for i in range(g):
        length = len(dragon)
        endx, endy = next_endx, next_endy
        for j in range(length):
            tmpx, tmpy = dragon[j]
            if (tmpx, tmpy) != (endx, endy):
                disx = endx - tmpx
                disy = endy - tmpy
                disx, disy = rotate(disx, disy)
                nextx, nexty = endx - disx, endy - disy
                dragon.append([nextx, nexty])
                m[nexty][nextx] = n
            if j == 0:
                next_endx, next_endy = nextx, nexty


N = int(input())
m = [[0] * 101 for _ in range(101)]
for i in range(N):
    x, y, d, g = map(int, input().split())
    gen(x, y, d, g, i + 1)

result = 0
for i in range(100):
    for j in range(100):
        if m[i][j] and m[i][j + 1] and m[i + 1][j] and m[i + 1][j + 1]:
            result += 1
print(result)