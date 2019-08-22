def find(string):
    idx = 0
    flag = False
    verify = 0
    result = 0
    while idx < len(string):
        tmp = string[idx: idx + 7]
        num = code[tmp]
        if flag:
            verify += num
        else:
            verify += num * 3
        result += num
        flag = not flag
        idx += 7
    if verify % 10:
        return 0
    return result


code = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
        '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    m = [input() for _ in range(N)]
    end = 0
    for i in range(N):
        for j in range(M):
            if m[i][M - 1 - j] == '1':
                string = m[i][M - j - 56:M - j]
                result = find(string)
                end = 1
                break
        if end:
            break
    print("#{} {}".format(tc, result))