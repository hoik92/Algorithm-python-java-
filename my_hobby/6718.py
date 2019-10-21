for tc in range(1, int(input()) + 1):
    d = int(input())
    result = 0
    while True:
        if result == 5:
            break
        if d < 100:
            break
        d = d // 10
        if d == 0:
            break
        else:
            result += 1
    print("#{} {}".format(tc, result))