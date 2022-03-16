def enq(n):
    global last
    last += 1
    tree[last] = n # 완전 이진트리 유지
    c = last # 새로 추가된 정점을 자식으로
    p = c//2 # 완전이진트리에서의 부모 정점 번호
    while tree[p] < tree[c]: # 부모가 있고, 자식이 키값이 더크면 교환
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = tree[1] # 루트의 key 값
    tree[1] = tree[last]   # 마지막 정점 삭제
    last -= 1        # 마지막 정점의 삭제
    # 부모 > 자식 규칙 유지
    p = 1
    c = p * 2 # 왼쪽자식 노드 번호
    while c <= last: # 왼쪽 자식이 있으면
        if c+1<=last and tree[c] < tree[c+1]: # 오른쪽 자식노드도 있고 더 크면
            c += 1 # 오른쪽 자식 선택
        if tree[p] < tree[c]: # 자식의 키값이 더 크면 교환
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p*2

# 포화 이진트리의 정점번호 1~100
tree = [0]*(101)
last = 0