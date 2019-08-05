for tc in range(10):
    t = input()
    m = [list(map(int, input().split())) for _ in range(100)]
    idx = []
    result = 10000
    ans = 0

    for i in range(100):
        if m[0][i]:
            idx.append(i)
    for i in range(len(idx)):
        cur_idx = i
        tmp = 0
        for j in range(100):
            if cur_idx < len(idx) - 1 and m[j][idx[cur_idx] + 1]:
                tmp += idx[cur_idx + 1] - idx[cur_idx]
                cur_idx += 1
            elif cur_idx > 0 and m[j][idx[cur_idx] - 1]:
                tmp += idx[cur_idx] - idx[cur_idx - 1]
                cur_idx -= 1
            if tmp >= result:
                break
        if result > tmp:
            result = tmp
            ans = idx[i]
    print(f"#{t} {ans}")