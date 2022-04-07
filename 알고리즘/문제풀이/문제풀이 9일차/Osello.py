# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     osell = [[0]*N for _ in range(N)] # 오셀로 판
#     try_arr = [list(map(int, input().split())) for _ in range(M)] # 시도하는 좌표와 돌
#     k = N//2 # 시작 돌 찍기
#     osell[k-1][k-1], osell[k-1][k], osell[k][k-1], osell[k][k] = 2, 1, 1, 2 # 1이 흑돌, 2는 백돌
#     fin = 1
#     while try_arr and fin:
#         fin = 0
#         i, j, stone = try_arr.pop(0)
#         i, j = i-1, j-1
#         osell[i][j] = stone
#         for di, dj in [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]:
#             tmp = []
#             for k in range(1, N):
#                 ni, nj = i + di*k, j + dj*k
#                 if 0<=ni<N and 0<=nj<N and osell[ni][nj] != stone and osell[ni][nj] != 0:
#                     tmp.append((ni, nj))
#                 elif 0<=ni<N and 0<=nj<N and osell[ni][nj] == stone and tmp:
#                     while tmp:
#                         mi, mj = tmp.pop()
#                         osell[mi][mj] = stone
#                 else:
#                     break
#         for ti in range(N):
#             if 0 in osell[ti]:
#                 fin += 1
#
#
#     result_black, result_white = 0, 0
#     for i in range(N):
#         for j in range(N):
#             if osell[i][j] == 1:
#                 result_black += 1
#             elif osell[i][j] == 2:
#                 result_white += 1
#     print(f'#{tc} {result_black} {result_white}')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)] # 오셀로 판
    k = N//2 # 시작 돌 찍기
    arr[k][k], arr[k][k+1], arr[k+1][k], arr[k+1][k+1] = 2, 1, 1, 2 # 1이 흑돌, 2는 백돌
    for _ in range(M):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d
        for di, dj in [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]: # 방향 하나씩
            s = []
            for k in range(1, N): # 해당 방향을 끝까지 검사
                ni, nj = si+di*k, sj+dj*k #
                if 1<=ni<=N and 1<=nj<=N: # 검사 범위에 포함 되고
                    if arr[ni][nj] == 0: # 0이면 끝
                        break
                    elif arr[ni][nj] == d: #
                        for ci, cj in s:
                            arr[ci][cj]=d
                        break
                    else:
                        s.append((ni,nj))
                else:
                    break
    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{tc} {bcnt} {wcnt}')

