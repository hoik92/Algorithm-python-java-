def find_st_ba(num):
    global N
    for i in range(N):
        strike, ball = 0, 0
        for j in range(3):
            for k in range(3):
                if num[j] == int(q[i][k]):
                    if j == k:
                        strike += 1
                    else:
                        ball += 1
        if (strike, ball) != st_ba[i]:
            return False
    return True

N = int(input())
q = []
st_ba = []
for i in range(N):
    number, strike, ball = map(int, input().split())
    q.append(str(number))
    st_ba.append((strike, ball))

ans = 0
for i in range(1, 10):
    num = [i]
    for j in range(1, 10):
        if i != j:
            num.append(j)
            for k in range(1, 10):
                if i != j and j != k and k != i:
                    num.append(k)
                    result = find_st_ba(num)
                    if result:
                        ans += 1
                    num.pop()
            num.pop()
print(ans)