# def solution(N):
#     S = list(str(abs(N)))
#     if N >= 0:
#         for i in range(len(S)):
#             if int(S[i]) < 5:
#                 S.insert(i, '5')
#                 break
#         else:
#             S.append('5')
#     else:
#         for i in range(len(S)):
#             if int(S[i]) > 5:
#                 S.insert(i, '5')
#                 break
#         else:
#             S.append('5')
#     print(S)
# solution(65750)
# solution(-5159)
#
# print(655750 < 657550)
# print(-55159 < -51559)

def solution(A, B):
    a, b = int(A ** 0.5), int(B ** 0.5)
    cnt = 0
    if a * (a + 1) < A:
        cnt -= 1
    if b * (b + 1) <= B:
        cnt += 1
    cnt += b - a
    print(cnt)

solution(7, 7)