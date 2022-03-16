def pre_order(v):  # 전위순회
    if v:
        print((v)
        pre_order(ch1[v])
        pre_order(ch2[v])


def in_order(v):
    if v:
        in_order(ch1[v])
        print(v)
        in_order(ch2[v])


def post_order(v):
    if v:
        post_order(ch1[v])
        post_order(ch2[v])
        print(v)

# ```
# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
# ```
V = int(input()) # 마지막 정점 번호, 정점수. 만약 0번이 있는 경우 정점수는 마지막 번호 +1
E = V - 1
arr = list(map(int, input().split()))
# 부모를 인덱스로 자식번호 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
for i in range(E): # 부모-자식 E개의 쌍이 주어진 상태
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0: # 아직 자식이 없는 경우
        ch1[p] = c
    else:
        ch2[p] = c
# 여기까지 -부모를 인덱스로 자식 번호 저장
preorder_order()