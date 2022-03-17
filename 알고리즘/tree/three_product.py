for tc in range(1, int(input())+1):
    N = int(input())
    n = round(N**(1.0/3.0))
    if N == n**3:
        print(f'#{tc} {n}')
    else:
        print(f'#{tc} {-1}')