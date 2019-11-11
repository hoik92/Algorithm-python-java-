for tc in range(1, int(input()) + 1):
    n = int(input())
    result = [-1] * (n + 1)
    result[0] = 1
    result[1] = 1
    result[2] = 3
    for i in range(3, n + 1):
        result[i] = result[i - 1] + 2 * result[i - 2] + result[i - 3]
    print("#{} {}".format(tc, result[n]))