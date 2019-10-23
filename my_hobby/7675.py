for tc in range(1, int(input()) + 1):
    N = int(input())
    text = input().split()
    cnt = [0] * N
    idx = 0
    exception = ['.', '?', '!']
    for i in range(len(text)):
        string = text[i]
        isName = True
        nextText = False
        if len(string) != 1:
            for s in range(len(string)):
                if s == 0:
                    if not (65 <= ord(string[s]) <= 90):
                        isName = False
                elif s < len(string) - 1:
                    if not (97 <= ord(string[s]) <= 122):
                        isName = False
                else:
                    if string[s] in exception:
                        nextText = True
                    else:
                        if not (97 <= ord(string[s]) <= 122):
                            isName = False
        else:
            if not (65 <= ord(string[0]) <= 90):
                isName = False
            if string[0] in exception:
                isName = False
                nextText = True

        if isName:
            cnt[idx] += 1
        if nextText:
            idx += 1

    print("#{}".format(tc), end=" ")
    for i in range(N):
        print(cnt[i], end=" ")
    print()