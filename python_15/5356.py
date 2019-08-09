for tc in range(1, int(input()) + 1):
    m = [input() for _ in range(5)]
    max_len = 0
    for i in range(5):
        if len(m[i]) > max_len:
            max_len = len(m[i])

    result = ''
    for i in range(max_len):
        for j in range(5):
            if i < len(m[j]):
                result += m[j][i]
    print(f"#{tc} {result}")