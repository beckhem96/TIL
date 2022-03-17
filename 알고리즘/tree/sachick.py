for tc in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    tree = [0]*(N+1) # 노드에 값 저장
    par = [0]*(N+1) # 부모 노드 저장
    for i in range(N): # tree에 값 넣어주기
        if arr[i][1].isdigit(): # 피연산자면
            tree[int(arr[i][0])] = int(arr[i][1]) # 문자열 -> 정수로 저장
        else:
            tree[int(arr[i][0])]  = arr[i][1] # 연산자는 그대로 저장

    for i in range(N): # 자식 노드 확인
        if len(arr[i]) == 3: # 길이가 3이면 자식 하나
            par[int(arr[i][2])] = int(arr[i][0]) # par의 index가 자식 노드, value에는 부모노드 저장
        if len(arr[i]) == 4: # 길이가 4면 자식 둘
            par[int(arr[i][2])] = int(arr[i][0])
            par[int(arr[i][3])] = int(arr[i][0])
    stack = [] # 피연산자 받아줄 스택
    parnode = [] # 부모 노드 받아줄 스택
    yunsanja = '' # 연산자
    x, y = 0, 0
    for i in range(len(tree)-1, 0, -1): # tree뒤에서 부터
        stack.append(tree[i]) # stack에 하나씩 저장
        if par[i] in parnode: # 부모노드 저장한 곳에 현재 i의 부모 노드가 있다면
            yunsanja = tree[parnode.pop()] # 부모노드에 있는 연산자를 가져옴
            x, y = stack.pop(), stack.pop() # 자식 노드 두개를 pop해서 저장
            if yunsanja == '+': # 연산
                tree[par[i]] = x + y
            elif yunsanja == '-':
                tree[par[i]] = x - y
            elif yunsanja == '/':
                tree[par[i]] = x / y
            elif yunsanja == '*':
                tree[par[i]] = x * y
        else: # 부모노드 저장한 곳에 현재 i의 부모 노드가 없다면 parnode에 저장
            parnode.append(par[i])
    print(f'#{tc} {int(stack[0])}')

#완전 이진 아닌줄 알고 짠 코드
# def postorder(v):
#     L, R = 0, 0
#     if v<=N:
#         postorder(v*2)
#         if v*2<=N:
#             L = tree[v*2]
#         postorder(v*2+1)
#         if v*2<=N:
#             R = tree[v*2+1]
#         if tree[v] == '+':
#             tree[v] = L + R
#         elif tree[v] == '-':
#             tree[v] = L - R
#         elif tree[v] == '/':
#             tree[v] = L / R
#         elif tree[v] == '*':
#             tree[v] = L * R
# for i in range(1, 11):
#     tc = i
#     N = int(input()) # 후위순회 써야함
#     arr = [list(input().split()) for _ in range(N)]
#     tree = [0]*(N+1) # 노드에 값 저장
#     par = [0]*(N+1) # 부모 노드 저장
#     for i in range(N):
#         if arr[i][1].isdigit():
#             tree[int(arr[i][0])] = int(arr[i][1])
#         else:
#             tree[int(arr[i][0])]  = arr[i][1]
#
#     postorder(1)
#
#     print(f'#{tc} {int(tree[1])}')
