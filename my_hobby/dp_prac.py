def bino(n, k):
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i - 1][j - 1] + B[i - 1][j]
    return B[n][k]


B = [[-1] * 10 for _ in range(10)]

print(bino(5, 3))
print(B)
