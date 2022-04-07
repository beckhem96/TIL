'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def dfs(v, V): # 재귀
    visited[v] = 1
    print(v, end = ' ')
    for w in range(1, V+1):
        if adjM[v][w]==1 and visited[w]==0:
            dfs(w, V)

def dfs2(v, V):
    stack = [v]             # 스택생성 + 시작정점 push
    visited = [0]*(V+1)
    visited[v] = 1          # push됨 표시
    while stack:
        v = stack.pop()
        print(v)            # visit()
        for w in range(1, V+1):
            if adjM[v][w]==1 and visited[w]==0: # 인접하고 미방문 w
                stack.append(w)         # 갈림길 목록
                visited[w] = 1

def dfs2_adjL(v, V):    # 인접 리스트인 경우
    stack = [v]             # 스택생성 + 시작정점 push
    visited = [0]*(V+1)
    visited[v] = 1          # push됨 표시
    while stack:
        v = stack.pop()
        print(v)            # visit()
        for w in adjL[v]:   # v에 인접한 정점 w
            if visited[w]==0: # 인접하고 미방문 w
                stack.append(w)         # 갈림길 목록
                visited[w] = 1

def dfs3(v, V):
    stack = [v]             # 스택생성 + 시작정점 push
    visited = [0]*(V+1)
    while stack:
        v = stack.pop()
        if visited[v]==0:
            print(v)            # visit()
            visited[v] = 1
            for w in range(1, V+1):
                if adjM[v][w]==1 and visited[w]==0: # 인접하고 미방문 w
                    stack.append(w)         # 갈림길 목록


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjM[n1][n2] = 1
    #adjM[n2][n1] = 1

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)
visited = [0]*(V+1)
dfs(1, V)
# dfs3(1, V)
# dfs2_adjL(1, V)
# print()
