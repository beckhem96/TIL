def mininum(v):
    global node
    node += 1 # 노드 1부터 시작해서 하나씩 증가
    tree[node] = v # 노드에 인자 더하기
    c = node # c에 노드 저장
    p = node//2 # 이진 트리니까 2로 나누면 부모 노드가 나옴, Ex) 2, 3이면 1
    while p>=1 and tree[p] > tree[c]:  # 부모 노드가 1보다 크고 자식 노드가 부모노드 보다 작으면 계속
        tree[p], tree[c] = tree[c], tree[p] # 값 바꾸고
        c = p # 현 부모노드를 자식 노드로 바꾸고 밑으로 위로 계속 탐색하는거
        p = c//2 # 부모노드도 바꿔준다

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    value = list(map(int, input().split()))
    tree = [0]*(N+1)
    node = 0 # 현 노드 위치
    for i in value: # 숫자들 삽입
        mininum(i)

    leaf = N # 마지막 노드
    c = N
    p = c//2
    result = 0
    while p != 0:  # 루트까지
        result += tree[p] # 부모노드 값 저장
        c = p
        p = c//2

    print(f'#{tc} {result}')