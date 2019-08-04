for tc in range(1, int(input()) + 1):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    result = -1
    for i in range(n):
        for j in range(i + 1, n):
            tmp = a[i] * a[j]
            if j == i + 1 and tmp <= result:
                break
            if result < tmp < 10:
                result = tmp
            elif tmp >= 10 and tmp > result:
                tmp_str = str(tmp)
                inc = True
                for k in range(len(tmp_str) - 1):
                    if int(tmp_str[k]) > int(tmp_str[k + 1]):
                        inc = False
                        break
                if inc:
                    result = tmp
    print(f"#{tc} {result}")