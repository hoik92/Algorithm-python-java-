for tc in range(1, int(input())+1):
    N = int(input())
    m = list(map(int, input().split()))
    max_val = 0
    min_val = 1000000

    for i in m:
        if i >= max_val:
            max_val = i
        elif i < min_val:
            min_val = i
    print("#{} {}".format(tc, max_val - min_val))