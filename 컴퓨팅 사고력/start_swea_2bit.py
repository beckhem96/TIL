T = int(input())
for tc in range(1, T+1):
    N, S = input().split()
    result = ''
    for i in S:
        result += f'{int(i, 16):04b}'
    print(f'#{tc} {result}')