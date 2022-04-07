def f(i, j):

    for ti in range(N): # K를 하나씩 공사해보자 N*N번
        for tj in range(N):
            if ti!=i or tj !=j: # 시작 지점이 아닐때
                for k in range(1, K+1):
                    arr[ti][tj] = arr[ti][tj] - k
                    # 여기부터는 최대 거리 찾기
                    v = [[0] * N for _ in range(N)] # 거리표시
                    visited = [[0] * N for _ in range(N)] # 방문표시
                    v[i][j], visited[i][j] = 1, 1
                    q = [(i, j)]
                    while q:
                        zi, zj = q.pop()
                        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
                            ni, nj = zi+di, zj+dj
                            if 0<=ni<N and 0<=nj<N and arr[ni][nj] < arr[zi][zj]:
                                q.append((ni, nj))
                                v[ni][nj] = v[zi][zj] + 1

                    for r in range(len(last_point)):
                        ri, rj = last_point[r]
                        result.append(v[ri][rj])

                    arr[ti][tj] = arr[ti][tj] + k


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    start_point, last_point = [], []
    result = []
    highest = 0
    lowest = 100000

    for i in range(N):
        for j in range(N):
            if arr[i][j] > highest:
                highest = arr[i][j]
            if arr[i][j] < lowest:
                lowest = arr[i][j]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == highest:
                start_point.append((i, j))
            if arr[i][j] == lowest:
                last_point.append((i, j))

    for i in range(len(start_point)):
        ci, cj = start_point[i]
        f(ci, cj)

    print(f'#{tc} {max(result)}')


