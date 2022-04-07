import sys

sys.stdin = open('supply.txt', 'r')

# BFS로 풀어야함
# def DFS(i, j, s):
#     global result
#     if i >= N-1 and j >= N-1 and result > s:
#         result = s
#         return result
#     elif result < s:
#         return
#     else:
#         for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
#             ni, nj = i + di, j + dj
#             if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0:
#                 v[ni][nj] = 1
#                 DFS(ni, nj, s + arr[ni][nj])
#                 v[ni][nj] = 0
#     return

def bfs(si, sj, ei, ej):
    q.append((si, sj))
    v[si][sj] = arr[si][sj]
    while q:
        ci, cj = q.pop(0)
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]>v[ci][cj]+arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj]
    return v[ei][ej]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    v = [[10000] * N for _ in range(N)]
    q = []
    print(f'#{tc} {bfs(0, 0, N-1, N-1)}')



