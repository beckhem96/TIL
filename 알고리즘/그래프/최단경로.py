def Dijkstra(s, N):
    U = [0] * (N + 1) # 거리가 결정된 정점을 표시
    U[s] = 1 # 출발 정점 거리 표시함

    for i in range(N + 1):
        D[i] = adjM[s][i]

    for _ in range(N): # 남은 정점만큼 반복
        minV = INF
        w = 0
        for i in range(N+1):
            if U[i] == 0 and minV > D[i]: # 거리 결정 안됐고 최단 거리 결정
                minV = D[i]
                w = i # 이동한 정점 저장
        U[w] = 1 # 거리 결정함 표시
        for n in range(N+1):
            if 0<adjM[w][n]<INF:

                D[n] = min(D[n], D[w]+adjM[w][n]) # 더한거랑 ~

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    INF = 1000000
    adjM = [[INF]*(N+1) for _ in range(N+1)] # 인접행렬을 모두 백만으로 채움

    for i in range(N+1): # 인접행렬 대각선 0으로 채우는 반복문
        adjM[i][i] = 0

    for _ in range(E): # 경로와 거리를 인접행렬에 저장
        ni, nj, distance = map(int, input().split())
        adjM[ni][nj] = distance

    D = [0] * (N + 1)
    Dijkstra(0, N)
    print(f'#{tc} {D[N]}')