def dfs(n, tmp):
    global N, result
    t, p = m[n][0], m[n][1]
    tmp += p
    if n + t > N:
        return
    if tmp > memo[n]:
        memo[n] = tmp
        result = tmp
    if tmp < memo[n]:
        return
    for i in range(n + t, N):
        dfs(i, tmp)


N = int(input())
m = [0] * N
for i in range(N):
    m[i] = list(map(int, input().split()))

result = 0
memo = [0] * N
for i in range(N):
    dfs(i, 0)

print(max(memo))