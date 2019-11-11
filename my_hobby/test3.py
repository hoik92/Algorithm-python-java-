from collections import deque


def solution(a, b, c, d):
    r = 0
    aa, bb, cc = a, b, c
    while cc:
        r = bb % cc
        bb = cc
        cc = r
    while bb:
        r = aa % bb
        aa = bb
        bb = r
    if d % aa:
        return -1
    if max([a, b, c]) < d:
        return -1

    q = deque()
    q.append([a, 0, 0, 1])
    q.append([0, b, 0, 1])
    q.append([0, 0, c, 1])
    history = [a * 1000000, b * 10000, c]
    while q:
        tmp = q.popleft()
        for i in range(3):
            if tmp[i] == d:
                return tmp[3]

        if tmp[0] < a:
            t = a * 1000000 + tmp[1] * 10000 + tmp[2]
            if not t in history:
                history.append(t)
                q.append([a, tmp[1], tmp[2], tmp[3] + 1])
        if tmp[0]:
            if tmp[1] < b:
                t0 = 0
                t1 = tmp[1] + tmp[0]
                if t1 > b:
                    t0 = t1 - b
                    t1 = b
                if t0 == d or t1 == d:
                    return tmp[3] + 1
                t = t0 * 1000000 + t1 * 10000 + tmp[2]
                if not t in history:
                    history.append(t)
                    q.append([t0, t1, tmp[2], tmp[3] + 1])
            if tmp[2] < c:
                t0 = 0
                t2 = tmp[2] + tmp[0]
                if t2 > c:
                    t0 = t2 - c
                    t2 = c
                if t0 == d or t2 == d:
                    return tmp[3] + 1
                t = t0 * 1000000 + tmp[1] * 10000 + t2
                if not t in history:
                    history.append(t)
                    q.append([t0, tmp[1], t2, tmp[3] + 1])
            t = tmp[1] * 10000 + tmp[2]
            if not t in history:
                history.append(t)
                q.append([0, tmp[1], tmp[2], tmp[3] + 1])
        if tmp[1] < b:
            t = tmp[0] * 1000000 + b * 10000 + tmp[2]
            if not t in history:
                history.append(t)
                q.append([tmp[0], b, tmp[2], tmp[3] + 1])
        if tmp[1]:
            if tmp[0] < a:
                t1 = 0
                t0 = tmp[0] + tmp[1]
                if t0 > a:
                    t1 = t0 - a
                    t0 = a
                if t0 == d or t1 == d:
                    return tmp[3] + 1
                t = t0 * 1000000 + t1 * 10000 + tmp[2]
                if not t in history:
                    history.append(t)
                    q.append([t0, t1, tmp[2], tmp[3] + 1])
            if tmp[2] < c:
                t1 = 0
                t2 = tmp[2] + tmp[1]
                if t2 > c:
                    t1 = t2 - c
                    t2 = c
                if t1 == d or t2 == d:
                    return tmp[3] + 1
                t = tmp[0] * 1000000 + t1 * 10000 + t2
                if not t in history:
                    history.append(t)
                    q.append([tmp[0], t1, t2, tmp[3] + 1])
            t = tmp[0] * 1000000 + tmp[2]
            if not t in history:
                history.append(t)
                q.append([tmp[0], 0, tmp[2], tmp[3] + 1])
        if tmp[2] < c:
            t = tmp[0] * 1000000 + tmp[1] * 10000 + c
            if not t in history:
                history.append(t)
                q.append([tmp[0], tmp[1], c, tmp[3] + 1])
        if tmp[2]:
            if tmp[0] < a:
                t2 = 0
                t0 = tmp[0] + tmp[2]
                if t0 > a:
                    t2 = t0 - a
                    t0 = a
                if t0 == d or t2 == d:
                    return tmp[3] + 1
                t = t0 * 1000000 + tmp[1] * 10000 + t2
                if not t in history:
                    history.append(t)
                    q.append([t0, tmp[1], t2, tmp[3] + 1])
            if tmp[1] < b:
                t2 = 0
                t1 = tmp[1] + tmp[2]
                if t1 > b:
                    t2 = t1 - b
                    t1 = b
                if t1 == d or t2 == d:
                    return tmp[3] + 1
                t = tmp[0] * 1000000 + t1 * 10000 + t2
                if not t in history:
                    history.append(t)
                    q.append([tmp[0], t1, t2, tmp[3] + 1])
            t = tmp[0] * 1000000 + tmp[1] * 10000
            if not t in history:
                history.append(t)
                q.append([tmp[0], tmp[1], 0, tmp[3] + 1])