# def bfs(n, m):
#     v = [0]*1000001
#     q = [0]*1000001
#     front = -1
#     rear = -1
#     rear += 1
#     q[rear] = n
#     while front != rear:
#         front += 1
#         n = q[front]
#         if n == m:
#             return v[n]
#         t = [n-1, n+1, n*2, n-10]
#         for i in range(4):
#             if t[i]>0 and t[i]<=1000000:
#                 if v[t[i]] == 0:
#                     v[t[i]] = v[n] + 1
#                     rear += 1
#                     q[rear] = t[i]
#
# def bfs(n):
#     v = [0]*1000001
#     q = [0]*1000001
#     front = -1
#     rear = 0
#     q[rear] = n
#     while front != rear:
#         front += 1
#         n = q[front]
#         if n == M:
#             return v[n]
#         op = [n-1, n+1, n*2, n-10]
#         for k in range(4):
#             if  0 < op[k] <=1000000 and not v[op[k]]:
#                 v[op[k]] = v[n] + 1
#                 rear += 1
#                 q[rear] = op[k]


def bfs(n):
    q = [n]
    while q:
        n = q.pop(0)
        if n == M:
            return v[n]
        for k in [n-1, n+1, n*2, n-10]:
            if  0 < k <=1000000 and not v[k]:
                v[k] = v[n] + 1
                q.append(k)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    v = [0] * 1000001
    print(f'#{tc} {bfs(N)}')