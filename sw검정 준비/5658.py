htd = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
       '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
def hex_to_dec(mm):
    global n
    for i in range(len(mm)):
        tmp = 0
        for j in range(n):
            tmp += htd[mm[i][j]] * 16**(n - j - 1)
        mm[i] = tmp


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    m = list(input())
    can = []
    n = N // 4
    for i in range(0, N, n):
        can.append(m[i:i+n])

    for i in range(n - 1):
        tmp = m.pop()
        m.insert(0, tmp)
        for j in range(0, N, n):
            tmp2 = m[j:j+n]
            if not tmp2 in can:
                can.append(tmp2)

    hex_to_dec(can)
    result = sorted(can, reverse=True)
    print("#{} {}".format(tc, result[K - 1]))