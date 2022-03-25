# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7ZLNLanmYDFAS2&contestProbId=AXHN_JW6YWEDFAXR&probBoxId=AX-5UBpq3FQDFARi&type=USER&problemBoxTitle=220324_Start%EC%8B%A4%EC%8A%B5&problemBoxCnt=2
T = int(input())
for tc in range(1, T+1):
    N = float(input())
    s = ''
    cnt = 0
    while N:
        cnt += 1
        if cnt >= 13:
            s = 'overflow'
            break
        N = N * 2
        if N >= 1:
            s += '1'
            N = N - 1
        else:
            s += '0'
    print(f'#{tc} {s}')
