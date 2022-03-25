T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    q = []
    for i in range(1, N+1):
        q.append((arr.pop(0), i)) # (치즈양, 치즈의 숫자)
    i = N
    while q:
        out_pizza = q.pop(0)  # 피자 하나 빼서
        if out_pizza[0]//2 != 0:    # 녹은 치즈가 0이 아니면
            q.append((out_pizza[0]//2, out_pizza[1])) # 그대로 화덕에 넣고
        elif out_pizza[0]//2 == 0:   # 녹은 치즈가 0인데
            if arr: # 넣을 피자가 있어
                i += 1
                q.append((arr.pop(0), i)) # 화덕에 새로운 피자 넣어주고
            else:  # 넣을 피자가 없어
                last_pizz_n = out_pizza[1]    # 지금 치즈 확인한 피자가 마지막 피자니까 저장
    print(f'#{tc} {last_pizz_n}')