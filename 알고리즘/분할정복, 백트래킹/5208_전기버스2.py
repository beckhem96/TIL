import sys

sys.stdin = open('전기버스2.txt', 'r')

# def f(i, cnt, k): # 내 풀이 시간초과
#     if i >= N:
#         return
#     else:
#         k += battery[i]
#         for j in range(i+1, i+k+1):
#             if j < N:
#                 if (k+battery[j]) >= N:
#                     dis[-1] = min(cnt, dis[-1])
#                 else:
#                     f(j, cnt+1, k)
#             else:
#                 return


T = int(input())

for tc in range(1, T+1):
    battery = list(map(int, input().split()))
    N = battery[0]
    dis = [N]*(N+1)
    # f(1, 1, 0)
    dis[1] = 0
    for i in range(1, N): # 배터리 하나씩 접근
        for j in range(i+1, i+battery[i]+1): # 해당 충전지에서 갈 수 있는 거리 까지
            if j<=N: # 정류장에 도착 안했으면
                dis[j] = min(dis[j], dis[i]+1) # 충전횟수랑 N중에 작은거 넣기
                # dis[i]은 충전한 횟수
                # for j 반복해도 전에 충전한거에서 +1한거라 값이 안변함
                # 만약에 cnt += 1 했으면 같은 충전횟수여도 누적되서 크게 나왔겠지
    print(f'#{tc} {dis[-1]-1}')