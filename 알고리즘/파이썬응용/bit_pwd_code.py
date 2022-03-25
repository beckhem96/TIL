# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AX7ZLNLanmYDFAS2&contestProbId=AV15FZuqAL4CFAYD&probBoxId=AX-02UzKW-ADFAVy&type=PROBLEM&problemBoxTitle=220323_Start&problemBoxCnt=2
# num_pattern = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
#                '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
# def bit_to_num(arr):
#     s =''
#     for i in range(len(arr)):
#         s += str(arr[i])
#     if s in num_pattern:
#         return num_pattern[s]
#     else:
#         return -1
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # N은 배열의 세로 크기, M은 배열의 가로크기
#     arr = [list(map(int, input())) for _ in range(N)]
#     K = M//7
#     result = 0
#     for i in range(N): #세로 길이만큼 반복
#         code = []
#         num_code = []
#         if 1 in arr[i]: # 한줄
#             for j in range(M-1, -1, -1): # 뒤에서부터 시작 왜냐면 코드의 맨뒤는 다 1, 종료선도 없음
#                 if arr[i][j] == 1:
#                     code = arr[i][j-55:j+1]  # 56개의숫자 저장
#                     for k in range(8): # 8코드 씩 확인
#                         if 0<=bit_to_num(code[k*7:k*7+7])<=9: # 숫자로 변환한게 0~9면
#                             num_code.append(bit_to_num(code[k*7:k*7+7]))
#                     if -1 not in num_code: # 정해진 코드가 저장되어 있다면
#                         odd, even = 0, 0
#                         for l in range(len(num_code)//2):
#                             odd += num_code[l*2] # 0부터 시작하는 리스트라 이게 홀수
#                             even += num_code[l*2+1] # 이게 짝수, 검증코드
#                         if ((odd * 3) + even) % 10 == 0:
#                             result = sum(num_code)
#                     break
#     print(f'#{tc} {result}')

# 김창영님 코드
T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    numbers = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6,
               '0111011': 7, '0110111': 8, '0001011': 9}
    lst = []
    for _ in range(n): # 세로길이만큼
        tmp = input()  # 코드 받고
        idx = 0
        if lst:  # lst가 비어있지않으면 계속?
            continue
        while idx < m - 7: # m까지 안한 이유는?
            idx += 1  # 시작점 찾기
            if tmp[idx:idx + 7] in numbers and not int(tmp[idx + 7]): # 7개씩 끊어서 확인하는데 그게 numbers에 있어 그리고 코드의 마지막이 0(1의부정)이야
                lst.append(numbers[tmp[idx:idx + 7]]) # 조건에 맞는 idx부터 7개의 코드를 lst에 넣어줌 거기가 시작점
                idx += 6  # idx도 7개의 비트 다음부터 할 수 있게 6 더해줌
    answer = sum(lst) if not (sum(lst) + 2 * sum(lst[0:7:2])) % 10 else 0
    print(f'#{t} {answer}')