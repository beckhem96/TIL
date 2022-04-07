#
# def dfs(i, j, s, n):
#     if n == 7:
#         nums.add(s)
#         return
#     if n > 7:
#         return
#     for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
#         ni, nj = i + di, j + dj
#         if 0<=ni<4 and 0<=nj<4:
#             dfs(ni, nj, s+str(arr[ni][nj]), n+1)
#     return
#
# T = int(input())
#
# for tc in range(1, T+1):
#     arr = [list(map(int, input().split())) for _ in range(4)]
#     v = [[0] * 4 for _ in range(4)]
#     # nums = []
#     nums = set()
#     for i in range(4):
#         for j in range(4):
#             v[i][j] = 1
#             dfs(i, j, str(arr[i][j]), 1)
#     print(f'#{tc} {len(nums)}')

def dfs(s):
    global cnt
    cnt += 1
    v[s] = 1
    for i in range(M):
        if arr[i*2] == s and not v[arr[i*2+1]]:
            dfs(arr[i*2+1])



N = int(input())
M = int(input())
arr = []
for i in range(M):
    a, b = map(int, input().split())
    arr.append(a)
    arr.append(b)
cnt = 0
v = [0] * (N+1)
dfs(1)
print(cnt-1)



