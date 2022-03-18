# def BFS(s):
#     q = []
#     v = [0] * 101
#
#     q.append(s)
#     v[s] = 1
#     sol = s
#
#     while q:
#         c = q.pop(0) # 방금 들어온 값
#         if v[sol] < v[c] or v[sol] == v[c] and sol < c:
#             sol = c
#         for j in range(1, 101):
#             if adj[c][j] and v[j] == 0:
#                 q.append(j)
#                 v[j] = v[c] + 1
#     return sol
#
#
# T = 10
# # for test_case in range(1, T + 1):
# N, S = map(int, input().split())
# lst = list(map(int, input().split()))
# # [1] Lst 연결값을 인접행렬에 저장
# adj = [[0] * 101 for _ in range(101)]
# for i in range(0, len(lst), 2):
#     adj[lst[i]][lst[i + 1]] = 1
# print(lst)
# print(adj)
    # ans = BFS(S)
    # print(f'#{test_case} {ans}')

def BFS(s):
    v = [0] * 101
    q = []

    q.append(s)
    v[s] = 1 # 방문 횟수
    sol = s # 시작 수, 부모 노드 같은 거 같음

    while q:
        c = q.pop(0)  # 큐에서 나온 수
        if v[sol] < v[c] or v[sol] == v[c] and sol < c: # 같은 시도 중 가장 큰 값 구하기
            sol = c
        for j in range(1, 101):
            if adj[c][j] and v[j] == 0: # adj 배열의 값이 1이고 방문한 적 없다면
                q.append(j)
                v[j] = v[c] + 1

    return sol



T = 10
for tc in range(1, T+1):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[0]*101 for _ in range(101)] # 표시 배열
    for i in range(N//2):
        adj[arr[i*2]][arr[i*2+1]] = 1
    ans = BFS(start)
    print(f'#{tc} {ans}')




