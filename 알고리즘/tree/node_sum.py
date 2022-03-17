def postorder(v):
    if v<=N:
        postorder(v*2)
        if v*2<=N:
            tree[v] += tree[v*2]
        postorder(v*2+1)
        if  v*2+1<=N:
            tree[v] += tree[v*2+1]

T = int(input())
for tc in range(1, T+1):
    N, M, result_node = map(int, input().split())
    leaf = []
    tree = [0]*(N+1)
    for _ in range(M):
        i, j = map(int, input().split())
        tree[i] = j


    postorder(1)
    print(f'#{tc} {tree[result_node]}')