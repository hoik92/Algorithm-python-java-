def rotate(n, d, drt):
    if 0 < n < 4 and m[n - 1][2] != m[n][6] and drt != -1:
        rotate(n + 1, -d, 1)
    if 1 < n < 5 and m[n - 1][6] != m[n - 2][2] and drt != 1:
        rotate(n - 1, -d, -1)
    if d == -1:
        tmp = m[n - 1].pop(0)
        m[n - 1].append(tmp)
    else:
        tmp = m[n - 1].pop()
        m[n - 1].insert(0, tmp)


m = [list(input()) for _ in range(4)]
K = int(input())

for i in range(K):
    n, d = map(int, input().split())
    rotate(n, d, 0)

result = 0
for i in range(4):
    if m[i][0] == '1':
        result += 1 << i
print(result)