# def can_queen(k): # 퀸을 놓을 수 있는 지 검사
#     for i in range(k): #
#         # 조건 1 : 같은 열에 퀸이 있는가
#         # 조건 2 : 두개의 행과 열을 각각 뺴주고 절대값이 같으면 대각선 -> 대각선인가
#         # 위 조건 중 하나라도 참이면 퀸 못 넣는 조건
#         if v[k] == v[i] or abs(v[k] - v[i]) == abs(k - i):
#             return False # 조건이 맞으면 퀸 못놓음
#     return True # 조건이 틀리면 퀸 놓을 수 있음
#
# def f(k):
#     global cnt
#     if k == N:
#         cnt += 1
#     else:
#         for i in range(N): # N만큼 반복
#             v[k] = i # k행의 열들에 N까지 넣어보고
#             if can_queen(k): # 조건에 맞으면
#                 f(k+1) # 다음행 진행
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     v = [0] * N # 퀸들을 첫번째 행에 N개 놓은 상태, v[i] = j 가 i, j에 퀸 놓았다는 뜻
#     cnt = 0
#     f(0)
#     print(f'#{tc} {cnt}')

def can_queen(ci, cj):
    # 위에 확인
    for i in range(ci-1, -1, -1):
        if arr[i][cj]:
            return 0
    # 왼쪽 상단 대각선 확인
    i, j = ci-1, cj-1
    while i>=0 and j>=0:
        if arr[i][j]:
            return 0
        i, j = i-1, j-1
    # 오른쪽 상단 대각선 확인
    i, j = ci-1, cj+1
    while i>=0 and j<N:
        if arr[i][j]:
            return 0
        i, j = i-1, j+1

    return 1

def DFS(n):
    global result
    if n==N: # 종료조건
        result += 1
        return

    for j in range(N): # 열 번호
        if can_queen(n, j):
            arr[n][j] = 1
            DFS(n+1) # 다음 행
            arr[n][j] = 0
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    result = 0
    DFS(0)
    print(f'#{tc} {result}')
