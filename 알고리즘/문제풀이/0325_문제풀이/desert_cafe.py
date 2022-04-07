import sys
sys.stdin = open('desert_cafe_input.txt', 'r')

# def DFS(n, ci, cj, v):
#     global si, sj, ans
#     if n==2 and ans>=len(v)*2:
#         return
#     if n > 3: # 종료 조건
#         return
#     if ci==si and cj==sj and n == 3 and ans<len(v): # 정답 갱신
#         ans = len(v)
#         return
#
#     for k in range(n, n+2):
#         ni, nj = ci+di[k], cj+dj[k]
#         if 0<=ni<N and 0<=nj<N and arr[ni][nj] not in v:
#             v.append((arr[ni][nj]))
#             DFS(k, ni, nj, v)
#             v.pop()
#
# di, dj = (1,1,-1,-1,1), (-1,1,1,-1,-1)
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = -1
#     for si in range(0, N-2):
#         for sj in range(1, N-1):
#             DFS(0, si, sj, [])
#     print(f'#{tc} {ans}')

# 내 풀이
def f(n, ci, cj, past):
    global si, sj, ans

    if n == 2 and ans >= len(past) * 2: # 조기 종료 조건 오른쪽 아래와 왼쪽 위 방향, 왼쪽 아래와 오른쪽 위방향의 이동 길이가 같음
        return
    if n > 3:# 종료조건, a
        return
    if ci == si and cj == sj and n == 3 and ans < len(past): # 이동거리 긴게 나오면 갱신
        ans = len(past)
        return

    for k in range(n, n+2): # 방향유지와 회전
        ni, nj = ci + di[k], cj + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in past:  # 범위 안벗어나고 먹은 적없으면
            past.append(arr[ni][nj])  # 저장해줌
            f(k, ni, nj, past)
            past.pop()
    else:
        return -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    di, dj = [[1, 1, -1, -1, 1],  [1, -1, -1, 1, 1]]
    cnt = 0
    for si in range(0, N-2):
        for sj in range(1, N-1):
            f(0, si, sj, [])

    print(f'#{tc} {ans}')