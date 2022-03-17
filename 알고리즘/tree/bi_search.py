def inorder(v):
    global value
    if v:
        inorder(ch1[v])
        result[v] = value # 중위순회로 result에 저장
        value += 1
        inorder(ch2[v])
T = int(input())
for tc in range(1, T+1):

    N = int(input()) # 노드 개수
    nodes = []      # 노드의 리스트
    par = [1]       # 현 부모 사용할 리스트
    tree = []       # 부모-자식 순으로 저장할 리스트
    for i in range(2, N+1):  # N 만큼 노드들 생성, 1은 루트니까 뺴준다
        nodes.append(i)
    v = 0   # 1 2 1 3 2 4 2 5 이렇게 저장해야하니 v*2, v*2+1을 위한 값
    while nodes:
        tree.append(par[-1])
        tree.append(nodes.pop(0))
        if nodes:  # N이 짝수면 오류나서 만든 조건, nodes가 비어있으면 break
            tree.append(par[-1])
            tree.append(nodes.pop(0))
            par.append(tree[v*2+1])
            v += 1
        else:
            break
    E = N - 1   # 간선의 수
    ch1 = [0]*(N+1) # 왼쪽 노드들
    ch2 = [0]*(N+1) # 오른쪽 노드들

    for i in range(E):
        p, c = tree[i*2], tree[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    result = [0]*(N+1) # 결과 저장할 리스트
    value = 1   # 결과 저장할 때 인데스 역할
    inorder(1)
    print(f'#{tc} {result[1]} {result[N//2]}')


# def in_order(v):
#     global last
#     if v <= N:
#         in_order(v * 2)
#         last += 1
#         tree[v] = last
#         in_order(v * 2 + 1)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     tree = [0] * (N + 1)
#     last = 0
#     in_order(1)
#     print(f'#{tc} {tree[1]} {tree[N // 2]}')