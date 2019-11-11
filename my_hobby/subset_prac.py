m = [5, 4, 6, 3]
v = [10, 40, 30, 50]
n = 4

max_val = 0
for i in range(1 << n):
    tmp_m = [0] * n
    tmp_v = [0] * n
    for j in range(n):
        if i & (1 << j):
            tmp_m[j] = m[j]
            tmp_v[j] = v[j]
    if sum(tmp_m) <= 10:
        result = sum(tmp_v)
        if result > max_val:
            max_val = result
print(max_val)


w = 10
K = [[-1] * (w + 1) for _ in range(n + 1)]
for i in range(n + 1):
    K[i][0] = 0
for i in range(w + 1):
    K[0][i] = 0

for i in range(1, n + 1):
    for j in range(1, w + 1):
        if m[i - 1] > j:
            K[i][j] = K[i - 1][j]
        else:
            K[i][j] = max(K[i - 1][j], K[i - 1][j - m[i - 1]] + v[i - 1])
print(K[n][w])
print(K)