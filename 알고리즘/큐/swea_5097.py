T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # for _ in range(M):
    #     arr.append(arr.pop(0))
    # print(f'{tc} {arr[0]}')
    print(f'{tc} {arr[N % M]}') # N % M 의 나머지가 회전하고 남은 수 만큼 더 가는 것