def bsearch(n, start, end):
    cnt = 0
    while start < end:
        cnt += 1
        mid = (start + end) // 2
        if mid == n:
            break
        elif n < mid:
            end = mid
        else:
            start = mid
    return cnt

for tc in range(1, int(input())+1):
    P, A, B = map(int, input().split())

    cntA, cntB = 0, 0
    start, end = 1, P

    cntA = bsearch(A, start, end)
    cntB = bsearch(B, start, end)

    if cntA < cntB:
        result = 'A'
    elif cntA > cntB:
        result = 'B'
    else:
        result = 0

    print("#{} {}".format(tc, result))