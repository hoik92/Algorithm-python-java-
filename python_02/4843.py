for tc in range(1, int(input())+1):
    N = int(input())
    n = list(map(int, input().split()))

    result = []
    for i in range(len(n)):
        min_val = 101
        max_val = 0
        min_idx = 0
        max_idx = 0
        for j in range(len(n)):
            if 101 > n[j] > max_val:
                max_val = n[j]
                max_idx = j
            if 0 < n[j] < min_val:
                min_val = n[j]
                min_idx = j
        result.append(max_val)
        result.append(min_val)
        n[max_idx] = 0
        n[min_idx] = 0
        if len(result) >= 10:
            break

    if len(result) >= 10:
        iter = 10
    else:
        iter = len(result)

    print("#{}".format(tc), end=' ')
    for i in range(iter):
        print(result[i], end=' ')
    print()