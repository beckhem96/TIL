# 16진수를 10진수로 바꾸지
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(input())
    s = ''
    for i in range(N):
        s += f'{int(lst[i], 16):04b}'
    s = list(map(int, s))
    result, k = 0, 0
    N = len(s) // 7
    print(f'#{tc}', end=' ')
    for i in range(N):
        for j in range(6, -1, -1):
            if s[i * 7:i * 7 + 7][j] == 1:
                result += 2 ** k
            k += 1
        print(result, end=' ')
        result, k = 0, 0
    print()