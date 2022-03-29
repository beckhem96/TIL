import sys

sys.stdin = open('최소합_input.txt', 'r')
# DFS -> 스택, BFS -> 큐
def dfs(i, j, num_sum):
    global result
    if i == N - 1 and j == N - 1 and result > num_sum:
            result = num_sum

    for di, dj in [[1, 0], [0, 1]]:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N:
            dfs(ni, nj, num_sum + arr[ni][nj])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)] # 방문기록
    si, sj = 0, 0
    result = 99999


    dfs(si, sj, arr[si][sj])
    print(f'#{tc} {result}')


# 조기 종료 조건 삽입

def dfs(i, j, num_sum):
    global result
    if i == N - 1 and j == N - 1 and result > num_sum:
            result = num_sum
    if num_sum > result:
        return
    for di, dj in [[1, 0], [0, 1]]:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N:
            dfs(ni, nj, num_sum + arr[ni][nj])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)] # 방문기록
    si, sj = 0, 0
    result = 99999


    dfs(si, sj, arr[si][sj])
    print(f'#{tc} {result}')

# 5188. 최소합, 조기 종료조건 있음
# def dfs(x, y, ssum):
#     global res
#     # 이동 좌표 (상, 우)
#     dx = [1, 0]
#     dy = [0, 1]
#     ssum += arr[x][y]  # 기본적인 더하기 작업
#     # 종료 조건 `1. 값 갱신 2. 백트래킹
#     if x == N - 1 and y == N - 1:
#         if ssum < res:
#             res = ssum
#         return
#     elif ssum > res:
#         return
#     # 탐색
#     for i in range(2):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx <= N - 1 and ny <= N - 1:
#             dfs(nx, ny, ssum)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     res = 10 * N * N  # 최대값
#     dfs(0, 0, 0)
#     print(f'#{tc} {res}')


# DP
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     dp = [[0] * N for _ in range(N)]
#     dp[0][0] = arr[0][0]
#     for i in range(0, N):
#         for j in range(0, N):
#             if i == 0 and 0 <= j - 1 < N:
#                 dp[i][j] = arr[i][j] + dp[i][j - 1]
#             elif j == 0 and 0 <= i - 1 < N:
#                 dp[i][j] = arr[i][j] + dp[i - 1][j]
#             elif 0 <= j - 1 < N and 0 <= i - 1 < N:
#                 dp[i][j] = arr[i][j] + min(dp[i - 1][j], dp[i][j - 1])
#
#     print(f'#{tc} {dp[N - 1][N - 1]}')